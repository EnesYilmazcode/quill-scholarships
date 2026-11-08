"""Grade essays against RUBRIC.md with the claude CLI.
Usage: python scripts/grade.py <essay.md or folder> [--jobs 6] [--out regrades]
An essay file starts with a header holding its prompt and word limit (see essays/ or the README).
The judge sees the prompt, the word limit and the essay, never the outcome."""
import argparse, io, json, os, re, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUDGE_ASK = """You are a strict scholarship judge. Score the essay below using ONLY this rubric.

=== RUBRIC ===
%s

=== SCHOLARSHIP PROMPT ===
%s

Word limit: %s. The essay has %d words.

=== ESSAY ===
%s

The writer only uses true events. Never suggest adding a scene, near miss, or detail that may not have happened; suggest cutting, sharpening, or reordering instead.

Reply with ONLY a JSON object, no prose and no code fence, in this shape:
{"total": <weighted total 0-100>, "criteria": [{"name": "<criterion>", "weight": <weight>, "score": <1-5>, "reason": "<one line>"}], "fixes": ["<fix 1>", "<fix 2>", "<fix 3>"]}"""


def parse(path):
    raw = io.open(path, encoding="utf-8").read().replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n(.*)", raw, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2).strip()


def grade(path, rubric, out_dir):
    name = os.path.basename(path)
    out = os.path.join(out_dir, name.replace(".md", ".json"))
    if os.path.exists(out):
        return name, "cached"
    meta, essay = parse(path)
    ask = JUDGE_ASK % (rubric, meta.get("prompt", ""), meta.get("word_limit") or "none",
                       len(essay.split()), essay)
    for _ in range(2):
        p = subprocess.run([shutil.which("claude"), "-p", "--output-format", "text"], input=ask,
                           capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=600, cwd=out_dir)
        s = p.stdout
        try:
            r = json.loads(s[s.index("{"):s.rindex("}") + 1])
            float(r["total"])
            break
        except (ValueError, KeyError, TypeError):
            r = None
    if r is None:
        return name, "FAILED " + (p.stdout or p.stderr)[-200:]
    r = {"file": name, "total": round(float(r["total"])), "criteria": r.get("criteria", []),
         "fixes": r.get("fixes", [])[:3]}
    tmp = out + ".tmp"
    json.dump(r, io.open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, out)
    return name, r["total"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--prefix", default="")
    ap.add_argument("--out", default=os.path.join(ROOT, "regrades"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rubric = io.open(os.path.join(ROOT, "RUBRIC.md"), encoding="utf-8").read()
    if os.path.isfile(a.src):
        files = [a.src]
    else:
        files = sorted(os.path.join(a.src, f) for f in os.listdir(a.src)
                       if f.endswith(".md") and f.startswith(a.prefix))
    with ThreadPoolExecutor(a.jobs) as ex:
        for name, res in ex.map(lambda f: grade(f, rubric, a.out), files):
            print(name, res, flush=True)


if __name__ == "__main__":
    main()
