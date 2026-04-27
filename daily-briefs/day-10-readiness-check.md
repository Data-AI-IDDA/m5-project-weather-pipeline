# Day 10 — Readiness Check & Final Preparation

## Overview

Today is **not** the in-class presentation (that is scheduled separately by the teaching team). Today is a **readiness day**: apply the fix list from yesterday's dress rehearsal, finalise the slide deck, freeze the team repo, and upload the PDF as the formal readiness signal.

By the end of today the project should be presentation-ready: deck exported, repo clean and accessible, demo deterministic, team aligned on who presents what.

## Today's Objectives

- Apply the fix list from the dress rehearsal.
- Run a final, lighter rehearsal to confirm the fixes landed.
- Freeze the project: clean repo, working `main`, complete `README.md`.
- Export the slide deck as a single PDF and upload it as the readiness deliverable.

## Tasks

### Task 1 — Apply Yesterday's Fix List

Work through the fix list from the dress rehearsal. Stay scoped — today is for polish and de-risking, not for adding new content. If something is fundamentally broken, fix it; if it is "nice to have", drop it.

### Task 2 — Confirmation Rehearsal (lighter, ~15 min)

After the fixes, run a shorter rehearsal — focus on the sections that were weakest yesterday and on the live demo. You are not trying to find new issues; you are confirming the fixes work.

### Task 3 — Repo Readiness

Make the team repo presentation-ready:

- `main` reflects the final state and runs end-to-end.
- Top-level `README.md` covers: project description, install steps, how to run the pipeline, headline results.
- All daily notebooks (`day_01` through `day_08`) run top-to-bottom without errors.
- `requirements.txt` is complete and pinned where reasonable.
- `reports/figures/` contains the figures used in the deck.
- Optionally tag the readiness snapshot, for example `v1.0-ready`.

Confirm both teaching-team members are still listed as collaborators on the repo:

- `alexander.poplavsky@ironhack.com` (Alexander)
- `jannat.samadov@gmail.com` (Jannat)

### Task 4 — Export and Upload the Presentation PDF (readiness signal)

- Export your slide deck as a **single PDF** (one team-wide file, not one per member).
- Upload it as the **Project 1 – Readiness Check & Final Preparation** deliverable in the Student Portal.
- Keep a copy in the repo as well — for example `reports/final_presentation.pdf`.

This PDF upload is your team's formal readiness signal: it tells the teaching team you are ready to present. It is the **only graded submission** for Project 1. Grading is manual — there is no AI grading and no portal due-time. The actual in-class presentation happens on a separate day announced by the teaching team and may include further small fixes after today, but the version uploaded today should already stand on its own.

## Deliverable

- [x] Final slide deck exported as a single PDF and uploaded in the Student Portal.
- [x] `main` clean, runnable end-to-end, with a complete top-level `README.md`.
- [x] Teaching team listed as collaborators on the team repo.
- [x] Optional: `v1.0-ready` tag on `main`.

## Resources

- [Google Slides — download as PDF](https://support.google.com/docs/answer/40608?hl=en)
- [PowerPoint — save as PDF](https://support.microsoft.com/en-us/office/save-or-convert-to-pdf-or-xps-d85416c5-7d77-4fd6-a216-6f4bf7c7c110)
- [Jupyter Slides export with `nbconvert`](https://nbconvert.readthedocs.io/en/latest/usage.html#convert-slides)
