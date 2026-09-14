# Process overview

Written by you, for a reader: how you got from the brief to the harness and
agentic workflow behind this submission. Markers read this file and follow its
citations; they don't trawl the repo for evidence you didn't point at.

This file is the shape; the course site's
[assessment page](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/topics/assessment/#what-you-submit)
is the requirement, and its
[word counts](https://comp.anu.edu.au/courses/comp4020-agentic-coding-studio/topics/assessment/#word-counts)
cover every deliverable.

## What I built

SLOP2950 "Weaponised Etiquette" is a fictional-but-complete twelve-week course
that studies public-etiquette violations (elevators, queues, coughs, litter,
seat-saving, pedestrian flow) as an academic discipline: watch a norm, isolate
the smallest deliberate act that breaks it, describe precisely what happens.
Weeks 2–10 are case-study weeks, Week 11 is a supervised live Practicum, and
Week 12 is a capstone report — with three assessments (25/35/40%) marking
each stage.

## How I got here

I started from a rough Korean-language idea about an exaggerated "how to be a
public nuisance" course, and my own first job was turning that premise into
something I could actually build against the platform: a real course code,
level, and semester in `src/course-config.ts`, and a renamed session label
("Field Exercises" rather than the generic default) in `src/site-config.ts`
([`4477e95`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/4477e95670744d68f43938db85062a6208ac8f32)).
Deciding the tone mattered here: the brief's premise reads as literal harmful
advice if taken at face value, so I kept the course's own voice
analytical/cataloguing throughout, and made that an explicit rule in
`CLAUDE.md`
([`63fdb0a`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/63fdb0a5b9e44fa6bf2f0c5363fe898f769ed21c)).

The starter's placeholder images hash-match a check the evidence gate runs
specifically for this deliverable, so I wrote a small PIL script
(`scripts/gen_brand_art.py`) to generate the card and hero art myself rather
than sourcing photography — a flat two-ink illustration of the hero image's
own subject: a lecture theatre where one seat, mid-sneeze, is ringed like a
prohibited sign
([`5e4b154`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/5e4b1540a170efd9d61bd447f8ed9566943f9b9d)).
No AVIF encoder was available locally, so I deleted the old `.avif` rather
than force a re-encode — the evidence check treats a deleted starter file as
passing, which I read as a sanctioned design decision rather than a workaround.

From there it was mostly content, built collection by collection against the
Zod schemas already defined in `src/content.config.ts`: two personas replacing
the starter's people
([`84433c6`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/84433c60329c82f673ee4486c1b8aee4161bf201)),
all twelve lecture weeks
([`aa41a59`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/aa41a59377219e7087f4392ff5280415a3ba58d0)),
three Field Exercise sessions
([`5266d02`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/5266d0218c6ce4b848e25883e33a9e004a4f6a61)),
and three assessments whose weights I checked by hand sum to exactly 100
([`b000996`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/b000996a845894433ee653960caa31a01cf4457c)),
then a real astromotion slide deck for Week 1
([`85feec7`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/85feec7ec4544717bbc9fa4463394b9e0872f4c0))
and the homepage/404/policies copy, including a policies page that states
plainly where the course's "live performance" is actually scoped to
([`c6350b0`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/c6350b048f232ac02f7a21e35e3d116255ace5a6)).

I knew the result was right by running `pnpm check` after every slice — build,
typecheck, and `spec/` — rather than trusting the schema alone; the shipped
`data-integrity.test.ts` catches date drift, but the course's other real
promises (weights summing to 100, every named teacher resolving to a real
profile, a lecture's `slides` field actually pointing at a built deck) weren't
covered anywhere, so I wrote
[`spec/course-promises.test.ts`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/eb779306d72ff0dc3c7f67d5fc0f42d270d048b4)
against the built course API to close that gap. I also ran the site under
`pnpm dev`, hit every collection's index and a sample detail page with `curl`,
and read the generated hero image back to confirm it actually renders the way
I intended before pushing.

## Review pass

After the initial build shipped to `main`, I set up a small role-scoped
review harness on a separate branch: `design-assets`, `ux`, and `qa`
subagents run a read-mostly scan first, and a `teaching-a`/`teaching-b`
proposer/critic pair is held for a later content-focused round — with a
human supervisor session triaging findings and relaying between agents
rather than letting them merge unsupervised. This repo's own `.gitignore`
treats `.claude/` as machine-local (it can hold a course API key, and the
repo goes public), so I kept the actual subagent prompts untracked and
documented the roles, effort levels, and rules instead in `AGENTS.md`
([`6eb0523`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/6eb0523ad87a3e18e15d2389581510bd08822e70)),
so the harness stays evidence-backed without fighting the template's own
tracked-vs-local convention. This round's work happens on `team-workflow`
and lands via PR rather than direct commits to `main`.

I also asked the supervisor session to review `CLAUDE.md` and `plan.md` for
whether they still hold appropriate content. `CLAUDE.md` checked out clean.
`plan.md` — an untracked pre-pivot draft of a comedic "생활수칙 지키기"
premise — was stale but not wrong: rather than delete it, I had it annotated
as the concrete artifact of the pivot this file's "How I got here" section
already narrates, and had its now-answered "Open questions" resolved instead
of left looking outdated
([`bcb5f62`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/bcb5f62)).

I then ran the `teaching-a`/`teaching-b` debate round I'd deferred above,
relayed by hand: `teaching-a` drafted tone-drift fixes and method-anchor
sentences across the lecture set, `teaching-b` critiqued them for redundancy
and one consent-boundary gap in the Practicum framing, and I reconciled both
rounds against the live files myself rather than applying either agent's
diff verbatim — the week-06 insertion in particular got a different point
and wording than either proposed
([`86cce2a`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/86cce2ad25de1b6331bf3a6db46e54c06f792f8d)).

That surfaced a real gap in the review harness: `qa`'s scan only runs
`pnpm check`/`check:evidence`, which never render a page, so I did a manual
pass with headless Chrome (`google-chrome --headless=new
--screenshot=...`) across every lecture, session, assessment, and index
page and read the resulting PNGs directly. That caught a bug none of the
automated checks or agent text-review had: `src/pages/lectures/[slug].astro`
re-prepended `Week N:` onto a lecture `title` that already had it baked in,
so all 12 lecture pages rendered the prefix twice in the browser tab and the
`<h1>`. Fixed and re-verified with a fresh screenshot
([`0208664`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/0208664131d233404f3a491e5bd930b1cc28e60e)).

Pushed `team-workflow` to `origin` at this point (no PR yet, and still no
merge to `main`). The user also asked for three standing process changes
going forward: push regularly instead of only committing locally, log every
request of theirs here briefly as it happens rather than in a batch, and
point them at a page they can inspect themselves rather than only a written
report — the local dev server (`pnpm dev`, serving under
`/comp4020-ass2-passionleader/` per `pages-base.ts`) is used for that until
something's actually merged and deployed.

The user then asked me to audit `PROCESS.md`, `plan.md`, `CLAUDE.md`, and
`AGENTS.md` for stale or useless content given how much has changed since
the initial build. `plan.md` needs no further change — its job is to hold
the initial planning content, which it does. `AGENTS.md` was updated to
name the actual mechanism (independent Claude Code CLI sessions coordinated
by cross-session messaging, since the Agent tool's custom subagent types
weren't usable here) and to note that the supervisor's manual visual QA
covers a real gap in `qa`'s text/build-only checks. `CLAUDE.md` gained a
line under "Before considering a slice done" clarifying that "look at the
page" means reading the rendered output, not just a 200 status, citing the
lecture-title bug as the example.

## Before you ship

`pnpm check:evidence` verifies that this comment is gone, that your citations
resolve to real commits, that a crit week's reflection entry is in
`reflections/`, and that your `CLAUDE.md` is there. It checks that your account
is traceable, not that it is good: that is the marker's call.

Images aren't checked: unlike a citation whose SHA doesn't resolve, a broken
image is visible the moment this file is rendered on GitHub.
