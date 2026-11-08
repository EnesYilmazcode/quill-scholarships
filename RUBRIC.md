# Scholarship essay judge: rubric v1

Built 2026-11-07 from the per-essay analyses of all 217 corpus files in `research/corpus/`, plus `kanoski-winners.md`, `other-winners.md`, `ai-patterns.md` and `VOICE-PROFILE.md`. Every anchor quote below was checked against the corpus file it names.

## What the data is, and what it can prove

- 177 winners: Kanoski (kan-01 to kan-55), Marks & Harrison and Morris King & Hodge first places (7 of dd-01 to dd-20), law-firm and Bold.org scholarships (law, bold, boldb), JFK Profile in Courage and AFSA winners (gen), tech contest winners (6 of tech-01 to tech-14).
- 40 non-winners: 13 dd runners-up, 8 tech runners-up, and 19 neg files (14 posted Varsity Tutors entries that lost, 5 published "before editing" or "blunder" samples).
- Each file has analyst scores (1 to 5) for answers_prompt, specificity, originality, idea_mechanism, structure_flow, voice_humanness, plus an overall 1 to 10.

Two kinds of comparison are used:

1. **Outcome contrasts** (real judges decided): winners vs the 19 neg non-winners, and first place vs runner-up inside the same contest (dd and EngineerGirl).
2. **Strong vs weak winners** (analyst decided): the 32 winners with overall 8 or higher vs the 16 winners with overall 4 or lower. These tell us what separates a great winning essay from one that won against a thin field.

Caveats a judge should know. The 32 strong winners lean heavily on the JFK and AFSA contests (26 of 32 are gen files), which are analytic essays, so personal-essay anchors are taken from kan, dd and law files wherever possible. Kanoski picks 5 winners a term from a small pool and visibly does not filter AI phrasing (11 of 55 Kanoski winners score voice 2 or lower), so "it won Kanoski" is a low bar. Over-limit essays still won (law-01 at 1,139 words on a ~1,000 limit, gen-44 at 1,351 on 1,250), so word-limit rules below are his compliance rule, not a quality signal from the data.

## Criteria and weights (sum 100)

| # | Criterion | Weight |
|---|---|---|
| 1 | Answers every part of the prompt directly | 20 |
| 2 | Specific, checkable detail | 20 |
| 3 | Human voice / no AI slop | 20 |
| 4 | One or two on-topic stories that carry the essay | 15 |
| 5 | Ideas with a mechanism (or, for reflective prompts, reasoning with a mechanism) | 15 |
| 6 | Structure, and an ending that returns to the opening | 10 |

Why these weights:

- **Answers the prompt (20).** The cleanest split in the whole set. All 32 strong winners score 5; none of the 16 weak winners do. On outcome, 8 of 19 non-winners score 2 or lower, against only 5 of 177 winners (bold-05, boldb-01, boldb-02, boldb-09, law-18). Mensa judges say the same: "Great writing can't save an essay that doesn't answer the question."
- **Specificity (20).** All 32 strong winners score 4 or 5; 15 of 16 weak winners score 2 or lower. On outcome, 13 of 19 non-winners score 2 or lower (mean 2.2). In the dd and EngineerGirl contests, first places average 3.8 against 3.3 for runners-up. This is also his own number-one tell (specificity collapse).
- **Human voice (20).** Outcome data: 28 of 177 winners (16%) score voice 2 or lower, against 9 of 19 non-winners (47%), and 9 of the 14 modern 2026 Varsity entries that lost. Same-contest: dd and EngineerGirl first places average voice 4.0 against 3.2 for runners-up. Among Kanoski winners, the 28 with voice 4 or higher average overall 6.0 against 4.7 for the 11 with voice 2 or lower. Weak winners: 8 of 16 score voice 2 or lower; strong winners: 2 of 32 (both in the Veritas philosophy contest, tech-05 and tech-07). Weighted at 20 rather than higher because Kanoski shows AI prose can still win a thin field; the payoff is standing out, not clearing the floor.
- **On-topic stories (15).** In the distracted-driving contests with first place and runners-up (dd), all 7 first places tell a real on-topic story; 5 of 13 runners-up tell none (dd-06, dd-08, dd-11, dd-16, dd-20). Personal-prompt winners with no story at all (13 files: law-07, law-09, law-11, bold-15, bold-17, bold-18, bold-19, bold-22, boldb-03, boldb-07, boldb-09, boldb-13, boldb-14) average overall 4.9. Off-topic material hurts: the analyses flag résumé recitals in law-02, law-05, law-06, law-17, bold-18 and boldb-10 (mean overall 5.75, none above 7), and dd-05 placed third with a hardship story "only loosely connected to distracted driving". Weighted 15, not 20, because the analytic JFK winners show a case study can do the job of a story.
- **Ideas with mechanism (15).** 31 of 32 strong winners score idea_mechanism 4 or 5; 15 of 16 weak winners score 2 or lower and none reach 4. But Kanoski winners almost all score 2 (only kan-25 and kan-48 reach 4), so on that contest the generic menu still wins. Weighted 15 as the strongest quality signal that is not yet a floor.
- **Structure and loop-back ending (10).** 31 of 32 strong winners score structure 4 or 5; 3 of 16 weak winners do. The 10 winners that close with "In conclusion" (kan-09, kan-29, kan-32, kan-33, kan-34, kan-35, law-11, law-12, law-19, boldb-13) average overall 4.4. The research files find the best winners loop back to the opening image (Parrott, Asmare, Fernanda). Weighted lowest because structure follows from getting 1 to 4 right.

## Scoring anchors

Score each criterion 1 to 5. 2 and 4 are in-between. Anchors quote the corpus file named.

### 1. Answers every part of the prompt directly (20)

Count the prompt's parts first (Kanoski has two: how it affected you, and ideas for young drivers). Every part must get its own substantive answer, early and plainly.

- **5.** Every part answered with its own section, including the hard part, and the answer is a position, not a gesture. law-14 answers "is the dream attainable" and concedes the cost: "The path is not equal, and the effort required is often greater."
- **3.** Every part touched, but one part gets a sentence. law-05 answers the attainability half in one closing line with no argument: "So, would I say that the American Dream is still achievable today? Absolutely, my parents are walking proof of the American Dream and what is possible, I am the American Dream."
- **1.** The essay is about something else. neg-11 was asked about a research question or project and opens: "We are all inevitably products of our environment." It never names a project.

### 2. Specific, checkable detail (20)

Every claim should carry a proper noun, a number, a physical detail, or a quoted fragment a stranger could not invent. Inventory facts beat outcome percentages (VOICE-PROFILE rule 2b).

- **5.** Dated, physical, unfakeable. kan-38: "On January 23rd, 2022 at 5:34 p.m. little did I know," followed by the smoking airbag and the 6-foot stranger at the window.
- **3.** One real felt detail, but no names, places or numbers around it. kan-04: "I found myself constantly checking my mirrors, worried that someone else might not be paying attention again."
- **1.** The central event is abstract. kan-34: "I vividly recall the day when I received the devastating news that a close friend had lost their life in a car accident caused by a distracted driver." No name, date, place or scene follows.

### 3. Human voice / no AI slop (20)

Run the `ai-patterns.md` checklist and his rules: no "not X but Y" or "isn't just X", no "not only X but also Y", no punchline closing every paragraph, no filler adverbs (truly, deeply, genuinely, incredibly), no em dashes, no AI vocabulary (delve, pivotal, multifaceted, foster, navigate, testament), no tidy moral at the end. Triage by density, not one hit. A draft over 250 words should have at least one sentence over 45 words (VOICE-PROFILE rule 1).

- **5.** Sounds like a specific person talking, including unflattering or clumsy moments. kan-16: "\"He'll be okay, there must be one serious dent in the car though\" I said back jokingly, unbeknownst to the consequences and severity of the truth."
- **3.** A human story wrapped in stock framing: triplets, a balanced antithesis, a slogan. kan-01: "It took away my sense of safety, but it gave me awareness and purpose."
- **1.** Interchangeable model prose, writing about itself. kan-29: "This essay delves into the profound impact of distracted driving".

### 4. One or two on-topic stories that carry the essay (15)

One story told fully, plus at most one small second beat from the writer's own behavior. Every story must serve the prompt. Unrelated achievements, résumé lists and off-topic hardship are flaws. For analytic prompts (JFK, AFSA), the case study is the story.

- **5.** One family story plus the writer's own slip, both on topic. dd-01 opens "My mother has told me this story so many times that I sometimes forget I wasn't there." and later admits unlocking his phone at a red light. kan-43 holds one loss and gets this close: "I try to imagine his voice, but as painful as it is to type I cannot remember it."
- **3.** The right story, told as a summary with no scene. kan-40: "She was my best friend." (the mother's death gets one phrase).
- **1.** No story, only a claim of one. boldb-03: "My friends often seek my advice on coping strategies, knowing I have developed effective techniques for managing mental health issues."

### 5. Ideas with a mechanism (15)

The winning formula from `other-winners.md`: name the existing fix, say why it fails, give a small concrete change, say who does it. A price or incentive is a plus. Generic menus (assemblies, social media campaigns, VR simulators, influencers) score 2 at best. For prompts with no ideas part, score the central reasoning the same way: does the essay explain why, not just that.

- **5.** A specific change with the reason people will actually do it. dd-01, on making phone driving mode default with an insurance cut: "People will rearrange their habits for a hundred bucks in a way they won't rearrange them for a PSA".
- **3.** Spots why the old fix fails, then offers a standard patch. kan-06: "Some apps can detect movement and lock the phone until the car stops. However, many teens either disable these features or forget to use them." (then gift cards and badges, no detail).
- **1.** Intent with no idea. kan-09: "I am passionate about promoting awareness around distracted driving."

### 6. Structure, and an ending that returns to the opening (10)

Clear paragraphs, a story at the front, ideas in the middle, and a close that brings back the opening person or image. Restating the thesis, "In conclusion", or a generic moral scores low.

- **5.** The last line pays off the opening. dd-01 opens on his mother's near miss and ends: "Three seconds saved my mom's life. I think we can build a world where three seconds isn't the difference."
- **3.** Organized, but the ending restates instead of returning. kan-26 opens on a dated crash and closes: "A combination of the aforementioned strategies, tailored to the specific needs and demographics of the target audience, can be highly effective in raising awareness of the dangers of distracted driving and preventing such instances among young drivers."
- **1.** One block, no arc. bold-12 is a single 480-word paragraph that opens: "A big point in my computer science education where I felt like I hit a wall was when I first went into the field."

## Automatic deductions

Subtract from the weighted total after scoring. Do not double-count with the criterion scores.

| Deduction | Points |
|---|---|
| Word limit exceeded (or under a stated minimum by more than 10%) | -10 |
| A prompt part with no answer at all (on top of a low criterion 1) | -10 per part |
| Negative disclaimer about the writer ("I haven't been in an accident", "my ability to code is worse than the average student"). His rule. Note the data: kan-18, kan-53 and bold-12 won with one, so this is a preference, not a measured penalty | -5 each, max -10 |
| Writing about the essay ("This essay explores", "In this essay I will") | -5 |
| Pasted prompt as line one, headings, bold or bullets in the essay | -5 |
| Em dash present (his rule: zero) | -2 each, max -6 |
| Fact that contradicts another document in his file (NUMBERS.md) or cannot be true | -10 |
| Chatbot residue ("Certainly!", "Here is a revised version") | -20 |

Floor the total at 0.

## Bands

- **high**: 72 to 100. Would place against a strong field.
- **mid**: 50 to 71. Could win a thin field, would lose to a strong one.
- **low**: under 50.

The gold set in `research/gold-set.json` is labeled with these bands, and the judge is calibrated when its bands match the gold set.

## Judge output format

Return exactly this, nothing else:

```json
{
  "file": "<file or draft name>",
  "scores": {
    "answers_prompt":   {"score": 1-5, "weight": 20, "reason": "<one line, quote the essay>"},
    "specificity":      {"score": 1-5, "weight": 20, "reason": "<one line>"},
    "human_voice":      {"score": 1-5, "weight": 20, "reason": "<one line, name the tells found>"},
    "stories":          {"score": 1-5, "weight": 15, "reason": "<one line, count the stories>"},
    "ideas_mechanism":  {"score": 1-5, "weight": 15, "reason": "<one line>"},
    "structure_ending": {"score": 1-5, "weight": 10, "reason": "<one line, quote the last line>"}
  },
  "weighted_subtotal": "<sum of score / 5 * weight, one decimal>",
  "deductions": [{"rule": "<name>", "points": -N, "evidence": "<quote>"}],
  "total": "<subtotal + deductions, floored at 0>",
  "band": "high | mid | low",
  "top_3_fixes": [
    "<most valuable fix first: what to change, where, and what to put there>",
    "<second>",
    "<third>"
  ]
}
```

Rules for the fixes: each one names a sentence or paragraph, says what to replace it with, and is ranked by points recovered (weight times score gap). Never suggest inventing a story or a number; suggest asking Enes for the real one.
