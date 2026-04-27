# Day 10 — Final Submission Day

## Overview

Today is **submission day**. Your team applies the last round of fixes from yesterday's dress rehearsal, freezes the project, and uploads the final presentation as a single PDF.

The actual class presentation is scheduled separately by the teaching team and will be announced — it is **not** today. Today's job is to ship a clean, presentable, frozen artifact.

## Today's Objectives

- Apply the fix list from yesterday's dress rehearsal.
- Freeze the project: clean repo, working `main`, complete `README.md`.
- Export the slide deck as a single PDF and upload it as the project deliverable.

## Tasks

### Task 1 — Apply the Fix List

Work through yesterday's fix list. Keep changes scoped — today is for polish and de-risking, not for adding new content. If something is fundamentally broken, fix it; if it is "nice to have", drop it.

### Task 2 — Final Repo Hygiene

Make sure your team repo is presentable:

- `main` reflects the final state and runs end-to-end.
- Top-level `README.md` covers: project description, install steps, how to run the pipeline, headline results.
- All daily notebooks (`day_01` through `day_08`) run top-to-bottom without errors.
- `requirements.txt` is complete and pinned where reasonable.
- `reports/figures/` contains the figures used in the presentation.
- Optionally tag the final snapshot, for example `v1.0-final`.

Confirm both teaching-team members are still listed as collaborators on the repo:

- `alexander.poplavsky@ironhack.com` (Alexander)
- `jannat.samadov@gmail.com` (Jannat)

### Task 3 — Export and Upload the Presentation PDF

- Export your slide deck as a **single PDF** (one team-wide file, not one per member).
- Submit it as the final deliverable for Project 1 in the Student Portal.
- Keep a copy in the repo as well — for example `reports/final_presentation.pdf`.

This PDF upload is the **only graded submission** for Project 1. Grading is manual by the teaching team — there is no AI grading and no due-time configured in the portal.

## Deliverable

- [x] Final slide deck exported as a single PDF and uploaded in the Student Portal.
- [x] `main` clean, runnable end-to-end, with a complete top-level `README.md`.
- [x] Teaching team listed as collaborators on the team repo.
- [x] Optional: `v1.0-final` tag on `main`.

## Resources

- [Google Slides — download as PDF](https://support.google.com/docs/answer/40608?hl=en)
- [PowerPoint — save as PDF](https://support.microsoft.com/en-us/office/save-or-convert-to-pdf-or-xps-d85416c5-7d77-4fd6-a216-6f4bf7c7c110)
- [Jupyter Slides export with `nbconvert`](https://nbconvert.readthedocs.io/en/latest/usage.html#convert-slides)
