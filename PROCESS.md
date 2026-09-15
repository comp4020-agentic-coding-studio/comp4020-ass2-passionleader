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

SLOP2950 "Weaponised Etiquette" is a fictional twelve-week course that treats
public-etiquette violations as an academic discipline: watch a norm, isolate
the deliberate act that breaks it, describe precisely what happens next. I
wanted the voice to read as a straight-faced, over-evaluated university
course — heavy on lecture/quiz/tutorial/assignment structure, light on
anything actually worth teaching — rather than a literal list of "how to
annoy people," so tone was a first-class constraint from the first commit
([`aa41a59`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/aa41a59377219e7087f4392ff5280415a3ba58d0),
[`85b99c2`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/85b99c2)).

## The breakthrough: a harness that has to look, not just pass

The real turning point wasn't a feature, it was a harness rule: I split the
work into role-scoped agents modelled on an actual small team —
design-assets, ux, qa, teaching-a, teaching-b — and told `qa` specifically to
open the rendered page with headless Chrome and read it, not just trust
`pnpm check`
([`6eb0523`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/6eb0523ad87a3e18e15d2389581510bd08822e70),
[`63fdb0a`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/63fdb0a5b9e44fa6bf2f0c5363fe898f769ed21c)).
That rule earned its keep almost immediately: a duplicated "Week N:" title had
shipped to all twelve lecture pages, invisible to every typecheck/build/test
run, and was only caught once a screenshot pass actually looked at the `<h1>`
([`0208664`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/0208664131d233404f3a491e5bd930b1cc28e60e)).

What the harness didn't do was save time the way I expected. Once revision
requests started stacking up — reframe a week, restyle a palette, redo a
photo set — coordinating five roles ran mostly sequentially rather than in
parallel, for noticeably more tokens than doing the same change in one
continuing session. The pattern that actually worked afterward was narrower:
build one sample end-to-end, show it to me, let me pick a direction, then
roll the rest out in that style — the Week 3 elevator slide went through
exactly that spike-then-rollout sequence before the other eight case-study
weeks followed it
([`df8a346`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/df8a346ae8ab7e18247fddd9104c0dc88141ef44),
later
[`1b36245`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/1b36245bc3eb59211334e64afc9fa971dbaa78d9),
[`e13cc1c`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/e13cc1c75e027505fea6aa8d8f5f2923d6427aca)).
The same discipline shaped content, not just images: tutorial "record your
reaction" prompts are built around the kind of before/after reaction people
already describe when this happens to them, rather than an invented scenario
([`557f3a5`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/557f3a53f1b5a5b1f3a42c1e35245f89ead17359)),
and deck photography moved from generated vector art to real, attributed
stock photography once the vector style stopped carrying a convincing
before/after beat on its own
([`df8a346`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/df8a346ae8ab7e18247fddd9104c0dc88141ef44)–[`e13cc1c`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/e13cc1c75e027505fea6aa8d8f5f2923d6427aca)).

## Reflection

**What was the breakthrough that moved the work forward?** Not a tool, a
constraint: forcing `qa` to look at the rendered screenshot instead of the
check output is what caught the duplicated-title bug that no automated pass
would have flagged
([`0208664`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/0208664131d233404f3a491e5bd930b1cc28e60e)).
The second, quieter breakthrough was noticing where the multi-agent harness
stopped paying for itself and replacing wholesale delegation with a
spike-first workflow instead
([`df8a346`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/df8a346ae8ab7e18247fddd9104c0dc88141ef44)).
A third showed up in content, not process: the model has no built-in sense
of what a believable "this is what manners is" moment sounds like, so every
tutorial's reaction beat had to be checked against how people actually
describe these moments in real discussion, not invented from a guess
([`557f3a5`](https://github.com/comp4020-agentic-coding-studio/comp4020-ass2-passionleader/commit/557f3a53f1b5a5b1f3a42c1e35245f89ead17359)).

**What did this change about who I want to be as a developer?** I started
this wanting to hand a whole course off to a "team" and check in at the end.
I came out of it wanting to run that team the way a PM would: deciding per
task whether the work actually needs five roles debating it, or one
continuing session showing me drafts to react to — instead of defaulting to
maximum delegation just because the harness makes it possible. The same
lesson applies to content, not just process: judging whether a "manner"
example is actually believable is still a call I have to make myself, not
one I can hand to the model.
