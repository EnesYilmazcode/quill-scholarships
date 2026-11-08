<h1 align="center">Quill Scholarships</h1>

<p align="center"><b>526 real scholarship essays, winners and losers, graded against one rubric.</b><br>
Quill is my scholarship writing desk. This repo is the data behind its judge: every essay scored blind, then checked against who actually won. Below that are the experiments that changed how Quill judges and writes.</p>

<p align="center">
  <img src="media/winner-vs-rest.png" width="560" alt="Dot chart: for each of 32 contests, how often the winner outscored a lower-placed essay. Earlier contests average 66%, new ones 51%.">
</p>

## How it works

1. **Collect.** Every essay comes from a page that published it: Bold.org winner pages, law-firm scholarship sites, essay contests that post their runners-up and finalists, and Varsity Tutors, which posts every entry along with the winner. Each one keeps its source link, its prompt, and the outcome the source states.
2. **Blind.** The judge sees the prompt, the word limit and the essay. It never sees the outcome, the contest name or the source.
3. **Grade.** `claude -p` scores the essay with [`RUBRIC.md`](RUBRIC.md): six criteria scored 1 to 5, weighted to 100, minus deductions for things like a blown word limit, em dashes, or chatbot residue. It also writes a one-line reason per criterion and three fixes.
4. **Check.** Inside one contest round the prompt and the judges are the same, so the fair test is simple: when a winner and a lower-placed essay share a round, does the winner score higher?

## System design

The grader is the same prompt as the Judge button in Quill, so a score here means the same thing as a score on a draft.

```mermaid
flowchart TB
  subgraph collect["Collecting"]
    S["Source pages: Bold.org, law firms, essay contests, Varsity Tutors"] --> E["Essay text + prompt + stated outcome + source link"]
  end
  subgraph grade["Grading, blind"]
    E --> B["Strip outcome and contest name"]
    B --> J["claude -p with RUBRIC.md"]
    J --> G["Score 0 to 100, six criterion scores with reasons, three fixes"]
  end
  subgraph check["Checking"]
    G --> P["Pair every winner with every lower-placed essay in its round"]
    P --> R["Winner higher in 60% of 387 pairs"]
  end
```

## Results

526 essays from 104 contests: 315 winners, 69 runners-up, 64 finalists, 27 honorable mentions, 46 entries that were not selected, and 5 with no stated outcome. 32 contests have both a winner and a lower-placed essay on the same prompt.

| Same-contest test | Contests | Pairs | Winner scored higher |
|---|---:|---:|---:|
| Earlier set (collected 2026-11-07) | 18 | 241 | 66% |
| New set (collected 2026-11-08) | 14 | 146 | 51% |
| **All** | **32** | **387** | **60%** |

Which criterion separates winners best, over the same 387 pairs:

| Criterion | Weight | Winner scored higher |
|---|---:|---:|
| Answers every part of the prompt | 20 | 62% |
| One or two on-topic stories | 15 | 61% |
| Specific, checkable detail | 20 | 57% |
| Ideas with a mechanism | 15 | 56% |
| Human voice, no AI slop | 20 | 55% |
| Structure, ending returns to the opening | 10 | 50% |

The judge is consistent. The 307 earlier essays were graded twice in separate runs: the scores correlate at 0.91, the median gap is 4 points, and 78% land in the same band (high, mid or low).

The honest part: the rubric measures quality, and quality only predicts a win a little. On the 14 new contests it was a coin flip. Winners average 55.0, finalists 58.0. Varsity Tutors (8 rounds) and The Nation (4 rounds) are where it misses most, and in both the losing entries are often just as polished as the winner. Counting only the prompt and story scores reaches 64%, but that weighting was picked after looking at the data, and the last reweighting tried here overfit (61% on held-out contests), so the v1 weights stay. Full per-contest table: [`results/VALIDATION.md`](results/VALIDATION.md).

So the rubric is a quality check, a way to catch a missed prompt part, vague detail, or AI phrasing, and not a promise to win. The experiments below found a judge that does better.

## Experiments

Four experiments, all scored against what real committees picked, never against my own rubric.

```mermaid
flowchart TB
  P["387 real pairs: a winner and a lower-placed essay from the same contest"] --> R["Referee: 'these two went to the same contest, which one won?' asked in both orders"]
  R --> V["Picks the real winner 72% of the time, rubric 60%"]
  B["11 real winners, one thing broken in each copy"] --> R
  C["Copies of real essays where Claude only fixed typos"] --> R
  W["Essays written for 10 past rounds by 5 writer versions"] --> G["Each one faces that round's real winner and up to 5 real entries"]
  G --> R
  V --> H["One-call committee score, guided by what the referee rewards"]
  H --> Q["Quill's Judge: 'beats N% of 259 real entries'"]
```

### 1. A judge that agrees with real committees

The rubric adds up six criteria. A judge with no rubric, asked only which of two essays won, picks the real winner far more often: Claude 72% over all 387 pairs, Gemini 3.1 Pro 80% on a random 100 (Claude 78% on those same pairs). A one-call version that scores a single essay, guided by the reasons the referee gave on pairs it got right, matches the pairwise referee. That one call is what Quill's Judge button runs now, next to the rubric.

<p align="center"><img src="media/judges.png" width="560" alt="Bar chart: rubric 59%, holistic no guidance 66%, holistic guided 68%, pairwise referee 68%"></p>

What the referee rewards that the rubric misses: a story of the kind the prompt asks for (a service prompt wants a story of helping someone, an academic prompt wants a real subject), fit with what the sponsor values, ideas that are the writer's own, one clear position, and clean copy.

**Is the referee just against AI text?** No. Against copies of real essays where Claude only fixed typos and grammar, it preferred the untouched original 46% of the time, a coin flip.

### 2. Break one thing, see who notices

53 edited copies of 11 strong real winners, one thing broken in each:

| Edit | Rubric total drop | Referee preferred the original |
|---|---:|---:|
| Strip names, numbers and places | 10.3 | 100% |
| Rewrite as AI prose | 5.5 | 100% |
| Remove the story | 13.5 | 95% |
| Swap in an "In conclusion" ending | 0.9 | 100% |
| Cut the answer to one prompt part | 7.2 | 100% |

The rubric notices every break but barely charges for AI prose or a flat ending. The referee catches all of them.

### 3. Backtest: write for a past round, drop it into the real pool

For 10 past rounds that published their losers, five writers each wrote an essay without seeing that round's entries. Each essay then faced the real winner and up to 5 real entries, judged by the referee in both orders. The writers that use my story bank only use facts I verified or told it directly.

<p align="center"><img src="media/writers.png" width="560" alt="Bar chart: plain AI 9%, AI plus rubric 13%, my real stories one pass 25%, four drafts plus tournament 21%, dictation slips cleaned 29%"></p>

Real stories beat invented ones by a wide margin. More drafting machinery did not help, and cleaning dictation slips ("I mean", spoken filler) did, though 10 rounds is small and the gaps between the last three bars are inside the noise. The losses mostly came from the story, not the prose: a prompt about helping someone answered with a startup story, or a distracted-driving contest where every winner had a first-person crash or phone-habit story and the bank had none.

### 4. What changed in Quill

- The Judge panel shows a committee read first: how many of 259 real contest essays the draft beats.
- Before drafting, the writer checks what kind of story past winners of that contest type told, and asks me for one if my story bank has none.
- Stories are chosen by the kind the prompt asks for, drafts are picked by committee read, and dictation slips get cleaned.

The experiment code runs against my private story bank, so it is not in this repo.

## Run it

```bash
python scripts/analyze.py                                # same-contest test from data/essays.csv
python scripts/analyze.py --md results/VALIDATION.md     # rewrite the results file
python scripts/grade.py my-essay.md                      # grade your own essay, needs the claude CLI
python scripts/grade.py essays/ --jobs 6                 # regrade a folder of essays
```

An essay file starts with a small header, then the text:

```
---
prompt: "How can we educate our community about the dangers of distracted driving?"
word_limit: 1000
---
My mother has told me this story so many times...
```

Grading takes about 30 seconds an essay on a Claude subscription, so all 526 take about an hour at 8 at a time.

The essay texts are not in this repo. They belong to the students who wrote them, so every grade links to the page where the essay was published instead.

| Folder | What's in it |
|---|---|
| [`contests/`](contests/) | one folder per contest, grouped into `law-firms`, `bold-org`, `essay-contests`, `varsity-tutors` and `other`. Each has a README with the prompt and a ranked table, and `grades/` with one JSON per essay |
| [`data/essays.csv`](data/essays.csv) | one row per essay: contest, outcome, words, total, all six criterion scores, first-run score, source link |
| [`results/`](results/) | the validation report |
| [`scripts/`](scripts/) | the grader and the analysis |
| [`media/`](media/) | the chart |

## Credits

Every essay was written by a student and published by its sponsor: Bold.org donors, Kanoski Bresney, Marks & Harrison, Morris King & Hodge, Parnall, Mushkatel Robbins & Becker, Younce Vtipil Baznik & Banks, Crowder, Mattis, Ramsay, Colombo, Jinks Crow, Rosen & Ohr, McKinney Tucker & Lemel, Neil Burns, the JFK Library Foundation, AFSA, the Elie Wiesel Foundation, the American Humanist Association, the Oxford Uehiro Centre, The Oxford Scientist, ASHG, Bow Seat, The Fountain, EngineerGirl, Americans Against Gun Violence, The Nation, Varsity Tutors, and the smaller contests listed under `contests/`. Links are in each grade file. Grading by [Claude](https://claude.com).
