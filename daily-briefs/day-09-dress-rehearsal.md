# Day 9 — Dress Rehearsal

## Overview

Today is **not** the final presentation. It is your **dress rehearsal**: a full, timed run-through of your presentation, end-to-end, with the goal of identifying everything that still needs to be fixed before the real thing.

The real presentation is scheduled separately by the teaching team and will be announced in class — it is **not** today and **not** tomorrow either. Tomorrow is the **readiness day**: you apply the fixes from today, freeze your PDF and your repo, and upload the readiness PDF. Use today to make tomorrow easy.

## Today's Objectives

- Deliver a complete dress rehearsal of your presentation, end-to-end, within the time budget.
- Catch issues — slides, demo, narration, timing — while there is still time to fix them.
- Decide which fixes you will apply on the readiness day and assign them within the team.

## Tasks

### Task 1 — Finalise the Slide Deck (Draft)

Your slides should already be drafted. Today, finalise them as a single deck, in the structure you'll actually present.

Cover, in order:

1. **Introduction (1–2 min)** — problem, cities, what "Can we trust this data?" means for your project.
2. **Data Pipeline (2–3 min)** — architecture diagram (from Day 5), data sources, database schema. Plan the live demo segment here.
3. **Data Quality Findings (2 min)** — key issues, how you handled them, your trust verdict.
4. **Statistical Analysis (2–3 min)** — most interesting EDA, hypothesis tests and correlations, feature selection highlights.
5. **Prediction Model (2–3 min)** — target, features, model comparison, best model performance with confidence intervals, prediction-vs-actual plot.
6. **Conclusions & Reflections (1–2 min)** — key takeaways, what you would do differently, your final answer to "Can we trust this data?".

Constraints:

- Slide deck format (Google Slides, PowerPoint, or Jupyter Slides), exportable to PDF.
- At least 5 figures from your own analysis (not screenshots of code).
- Code only briefly when explaining pipeline architecture.

### Task 2 — Run a Full Timed Rehearsal

Within your team, run the full presentation **once** end-to-end with a timer. Whoever is presenting each section presents that section for real. Do **not** stop in the middle to fix things — make notes and keep going.

- Target: ~10 minutes total.
- Include the live demo segment in the rehearsal (run the pipeline; show a prediction).
- One team member tracks time per section and writes down everything that goes wrong.

### Task 3 — Collect Feedback

Right after the rehearsal, capture in writing:

- Which sections went over time?
- Where did the narration falter or repeat itself?
- Did the live demo work? If not, why?
- Are there slides that are unreadable, too dense, or unnecessary?
- Are the figures legible at presentation size?

If a member of the teaching team is in the room, ask for one round of structured feedback.

### Task 4 — Plan Tomorrow's Fixes

End the day with a short, written **fix list** — each item assigned to a specific team member. This is what you will execute on the readiness day.

Examples:

- Cut slide 12, merge with slide 11.
- Re-export prediction-vs-actual plot at higher DPI.
- Rehearse the demo command sequence so it doesn't fail live.
- Clean up `README.md` so the repo is presentable.

## Deliverable

Push your work to your team repo. There is **no** graded submission today — tomorrow's PDF upload is the only graded deliverable for Project 1.

Recommended commits:

- [x] `slides/` (or equivalent) — current draft of your final deck.
- [x] `notebooks/day_09_rehearsal.ipynb` — short notebook capturing rehearsal feedback and the fix list (one cell per item, with the assignee).

## Resources

- [How to time a presentation](https://hbr.org/2014/06/how-to-give-a-killer-presentation)
- [Slide design tips for technical talks](https://speakerdeck.com)
- [matplotlib: tight layout and DPI for export](https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html)
