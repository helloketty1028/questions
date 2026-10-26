#!/usr/bin/env python3
"""Interview Bank — build indexes and validate links. Standard library only.

Usage:  python scripts/build_index.py [--resumes <path to resumes repo>]
Default resumes path: the sibling folder ../resumes  (C:\\Users\\surface\\resumes)
Writes: index/questions.md, index/coverage.md, index/stories.md, index/issues.md
Exit code 1 when any ERROR is found.
"""
import argparse, datetime, difflib, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TAX = {
    'industry': ['BNK', 'INT', 'TEL', 'COM'],
    'role': ['ATL', 'TPM', 'SM'],
    'qtype': ['BEH', 'DEEP', 'SYSDES', 'SITU', 'DOMAIN', 'MOTIV', 'RISK', 'REVERSE'],
    'evidence': ['direct', 'transferable', 'gap'],
    'priority': ['P1', 'P2', 'P3'],
}
Q_STATUS = {'draft', 'active', 'retired'}
S_STATUS = {'draft', 'verified', 'retired'}
FACT_RE = re.compile(r'(?:PA|X)-\d{2}(?:\.\d+)?')
TOKEN_RE = re.compile(r'"([^"]*)"|\'([^\']*)\'|([^,]+)')

issues = []  # (level, file, message)
def err(f, m): issues.append(('ERROR', f, m))
def warn(f, m): issues.append(('WARN', f, m))


def split_list(v):
    out = []
    for a, b, c in TOKEN_RE.findall(v):
        t = (a or b or c).strip()
        if t:
            out.append(t)
    return out


def parse_fm(path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^\ufeff?---\s*\n(.*?)\n---\s*(\n|$)', text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        k, sep, v = line.partition(':')
        if not sep:
            continue
        k, v = k.strip(), v.strip()
        if v.startswith('[') and v.endswith(']'):
            fm[k] = split_list(v[1:-1])
        else:
            fm[k] = v[1:-1] if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'' else v
    return fm


def as_list(fm, k):
    v = fm.get(k, [])
    return v if isinstance(v, list) else ([v] if v else [])


def load(folder, prefix):
    items = {}
    for p in sorted((ROOT / folder).glob('*.md')):
        rel = f'{folder}/{p.name}'
        fm = parse_fm(p)
        if fm is None:
            err(rel, 'missing frontmatter'); continue
        i = fm.get('id', '')
        if not i.startswith(prefix):
            err(rel, f'id "{i}" should start with {prefix}'); continue
        if i != p.stem:
            err(rel, f'file name must equal id ({i}.md)')
        if i in items:
            err(rel, f'duplicate id {i}')
        fm['_file'] = rel
        items[i] = fm
    return items


def load_topics():
    p = ROOT / 'governance' / 'taxonomy.md'
    if not p.exists():
        return set()
    t = p.read_text(encoding='utf-8')
    m = re.search(r'<!-- TOPICS:BEGIN -->(.*?)<!-- TOPICS:END -->', t, re.S)
    return set(re.findall(r'`([a-z0-9-]+)`', m.group(1))) if m else set()


def load_facts(resumes):
    p = Path(resumes) / 'master' / 'v2.0-draft' / '03_Achievement_Library.md'
    if not p.exists():
        warn('-', f'03_Achievement_Library.md not found at {p}; fact IDs not checked')
        return None, None
    facts, version = {}, None
    for line in p.read_text(encoding='utf-8').splitlines():
        if version is None:
            mv = re.search(r'\*\*Version:\*\*\s*(v[\d.]+)', line)
            if mv:
                version = mv.group(1)
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if cells and re.fullmatch(FACT_RE, cells[0]):
                status = cells[3] if '.' in cells[0] and len(cells) > 3 else cells[-1]
                facts.setdefault(cells[0], status)
        mh = re.match(r'^###\s+((?:PA|X)-\d{2})\b(.*)', line)
        if mh:
            facts.setdefault(mh.group(1), mh.group(2))
    return facts, version


def check_codes(rel, fm, key, multi=True, required=True):
    vals = as_list(fm, key) if multi else ([fm.get(key)] if fm.get(key) else [])
    if required and not vals:
        err(rel, f'{key} is empty')
    for v in vals:
        if v not in TAX[key]:
            err(rel, f'{key} "{v}" not in taxonomy {TAX[key]}')


def check_facts(rel, ids, facts):
    for f in ids:
        if not FACT_RE.fullmatch(f):
            err(rel, f'fact id "{f}" has wrong format (PA-01 / PA-01.2 / X-01)'); continue
        if facts is None:
            continue
        if f not in facts:
            err(rel, f'fact {f} not found in 03_Achievement_Library'); continue
        s = facts[f]
        if '⛔' in s or '⚠️' in s or '⚠' in s:
            err(rel, f'fact {f} status "{s}" — on hold / in conflict, must not be used')
        elif '❓' in s:
            warn(rel, f'fact {f} status "{s}" — use only the confirmed part')


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', s.lower()).strip()


def md_cell(s):
    return str(s).replace('|', '\\|')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--resumes', default=str(ROOT.parent / 'resumes'))
    a = ap.parse_args()

    topics = load_topics()
    facts, fver = load_facts(a.resumes)
    Q = load('questions', 'Q-')
    A = load('answers', 'A-Q')
    S = load('stories', 'S-')

    for i, q in Q.items():
        rel = q['_file']
        if not re.fullmatch(r'Q-\d{4}', i):
            err(rel, 'id format must be Q-0001')
        if not q.get('q'):
            err(rel, 'q is empty')
        for k in ('industry', 'role'):
            check_codes(rel, q, k)
        check_codes(rel, q, 'qtype', multi=False)
        check_codes(rel, q, 'priority', multi=False)
        if q.get('status') not in Q_STATUS:
            err(rel, f'status must be one of {sorted(Q_STATUS)}')
        for t in as_list(q, 'topics'):
            if topics and t not in topics:
                warn(rel, f'topic "{t}" not in taxonomy §6')
        ans = q.get('answer', '')
        if ans and ans != 'A-Q' + i[2:]:
            err(rel, f'answer should be A-Q{i[2:]}')
        if q.get('status') == 'active' and ans not in A:
            warn(rel, f'active question has no answer file {ans}')
        for s in as_list(q, 'stories'):
            if s not in S:
                err(rel, f'story {s} not found')
        if 'TEL' in as_list(q, 'industry') and A.get(ans, {}).get('evidence') == 'direct':
            warn(rel, 'TEL question with direct evidence — confirm 03 really has telecom evidence')

    for i, x in A.items():
        rel = x['_file']
        qid = x.get('question', '')
        if qid not in Q:
            err(rel, f'question {qid} not found')
        elif i != 'A-Q' + qid[2:]:
            err(rel, f'id should be A-Q{qid[2:]}')
        for s in as_list(x, 'stories'):
            if s not in S:
                err(rel, f'story {s} not found')
            elif S[s].get('status') != 'verified' and as_list(x, 'approved'):
                warn(rel, f'approved answer uses story {s} that is not verified')
        check_facts(rel, as_list(x, 'facts'), facts)
        for r in as_list(x, 'variants') + as_list(x, 'approved'):
            if r not in TAX['role']:
                err(rel, f'role "{r}" not in taxonomy')
        for r in as_list(x, 'approved'):
            if r not in as_list(x, 'variants'):
                err(rel, f'approved {r} is not in variants')
        if x.get('evidence') and x['evidence'] not in TAX['evidence']:
            err(rel, 'evidence must be direct / transferable / gap')

    for i, s in S.items():
        rel = s['_file']
        if not re.fullmatch(r'S-\d{3}', i):
            err(rel, 'id format must be S-001')
        if not as_list(s, 'facts'):
            err(rel, 'story has no fact ids')
        check_facts(rel, as_list(s, 'facts'), facts)
        for r in as_list(s, 'roles'):
            if r not in TAX['role']:
                err(rel, f'role "{r}" not in taxonomy')
        for r in as_list(s, 'industries'):
            if r not in TAX['industry']:
                err(rel, f'industry "{r}" not in taxonomy')
        if s.get('status') not in S_STATUS:
            err(rel, f'status must be one of {sorted(S_STATUS)}')
        fv = s.get('facts_version', '').replace('03', '').strip()
        if fver and fv != fver:
            warn(rel, f'written against 03 {fv or "?"}, current 03 is {fver} — recheck facts')

    # near-duplicate questions
    texts = [(i, norm(t)) for i, q in Q.items() if q.get('status') != 'retired'
             for t in [q.get('q', '')] + as_list(q, 'variants') if t]
    seen = set()
    for x in range(len(texts)):
        for y in range(x + 1, len(texts)):
            (i1, t1), (i2, t2) = texts[x], texts[y]
            if i1 != i2 and (i1, i2) not in seen and difflib.SequenceMatcher(None, t1, t2).ratio() >= 0.85:
                seen.add((i1, i2))
                warn(f'questions/{i1}.md', f'very similar to {i2} — merge or link as variant')

    used_by = {}
    for i, q in Q.items():
        for s in as_list(q, 'stories'):
            used_by.setdefault(s, []).append(i)

    today = datetime.date.today().isoformat()
    head = f'_Generated by scripts/build_index.py on {today} — do not edit by hand._\n\n'
    out = ROOT / 'index'
    out.mkdir(exist_ok=True)

    rows = ['| ID | Question | Industry | Role | Type | Topics | Pri | Stories | Answer | Status |',
            '|---|---|---|---|---|---|---|---|---|---|']
    for i, q in sorted(Q.items()):
        ans = q.get('answer', '')
        av = A.get(ans)
        astate = '—' if not av else (f"✔ {','.join(as_list(av, 'approved'))}" if as_list(av, 'approved') else 'draft')
        rows.append('| ' + ' | '.join(md_cell(c) for c in [
            i, q.get('q', ''), ','.join(as_list(q, 'industry')), ','.join(as_list(q, 'role')),
            q.get('qtype', ''), ', '.join(as_list(q, 'topics')), q.get('priority', ''),
            ','.join(as_list(q, 'stories')), astate, q.get('status', '')]) + ' |')
    (out / 'questions.md').write_text(f'# Question Index ({len(Q)})\n\n' + head + '\n'.join(rows) + '\n', encoding='utf-8')

    live = {i: q for i, q in Q.items() if q.get('status') != 'retired'}
    def cnt(pred):
        return sum(1 for q in live.values() if pred(q))
    cov = ['| Industry \\ Role | ' + ' | '.join(TAX['role']) + ' |', '|---|' + '---|' * len(TAX['role'])]
    for ind in TAX['industry']:
        cov.append(f'| {ind} | ' + ' | '.join(str(cnt(lambda q, r=r: ind in as_list(q, 'industry') and r in as_list(q, 'role')))
                                         for r in TAX['role']) + ' |')
    typ = ['| Type \\ Role | ' + ' | '.join(TAX['role']) + ' |', '|---|' + '---|' * len(TAX['role'])]
    for t in TAX['qtype']:
        typ.append(f'| {t} | ' + ' | '.join(str(cnt(lambda q, r=r: q.get('qtype') == t and r in as_list(q, 'role')))
                                       for r in TAX['role']) + ' |')
    appr = ['| Role | Answers with this variant | Approved |', '|---|---|---|']
    for r in TAX['role']:
        appr.append(f"| {r} | {sum(1 for x in A.values() if r in as_list(x, 'variants'))} | "
                    f"{sum(1 for x in A.values() if r in as_list(x, 'approved'))} |")
    (out / 'coverage.md').write_text(
        f'# Coverage\n\n{head}Live questions: {len(live)} · Answers: {len(A)} · Stories: {len(S)}\n\n'
        '## Industry × Role (questions)\n\n' + '\n'.join(cov) + '\n\n## Type × Role (questions)\n\n' + '\n'.join(typ) +
        '\n\n## Answer variants\n\n' + '\n'.join(appr) + '\n', encoding='utf-8')

    srows = ['| ID | Title | Facts | Roles | Industries | Evidence | Status | Used by |', '|---|---|---|---|---|---|---|---|']
    for i, s in sorted(S.items()):
        srows.append('| ' + ' | '.join(md_cell(c) for c in [
            i, s.get('title', ''), ', '.join(as_list(s, 'facts')), ','.join(as_list(s, 'roles')),
            ','.join(as_list(s, 'industries')), s.get('evidence', ''), s.get('status', ''),
            ', '.join(sorted(used_by.get(i, []))) or '—']) + ' |')
    (out / 'stories.md').write_text(f'# Story Index ({len(S)})\n\n' + head + '\n'.join(srows) + '\n', encoding='utf-8')

    ne = sum(1 for l, _, _ in issues if l == 'ERROR')
    nw = len(issues) - ne
    src = f'03_Achievement_Library {fver}' if fver else '03_Achievement_Library not read'
    lines = [f'# Issues — {ne} error(s), {nw} warning(s)\n', head + f'Fact source: {src} ({a.resumes})\n',
             '| Level | File | Issue |', '|---|---|---|']
    lines += [f'| {l} | {md_cell(f)} | {md_cell(m)} |' for l, f, m in sorted(issues)]
    (out / 'issues.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(f'questions={len(Q)} answers={len(A)} stories={len(S)} errors={ne} warnings={nw} ({src})')
    for l, f, m in sorted(issues):
        print(f'  {l}  {f}: {m}')
    return 1 if ne else 0


if __name__ == '__main__':
    sys.exit(main())
