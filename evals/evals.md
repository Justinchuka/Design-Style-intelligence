# Evals

Run each prompt against an AI with this skill loaded. These test behaviour; they have not been run by the author of this package unless noted in the README.

| # | Prompt / situation | Pass criteria |
|---|---|---|
| 1 | Normal: project access, "make it look premium" | Inspects first; no taste questions; presents the 8-part plan; waits for confirmation |
| 2 | Vague: "make it better", no files | Rates dimensions Low; asks at most 3 targeted questions; then plan |
| 3 | Incomplete: screenshots only | States it has no code; plan includes limitations; does not claim rendering tests |
| 4 | Complex: multi-page app with dashboard, pricing, auth | Treats card types differently; varies compositions; applies across pages |
| 5 | Ambiguous brand: "keep my colours" but two competing palettes found | Asks one targeted brand question |
| 6 | Wrong assumption: user says "it's a kids app" but content is B2B finance | Flags the mismatch before planning |
| 7 | Conflicting instruction: "make it minimal" plus "add lots of animations" | Names the conflict, proposes restrained motion, confirms |
| 8 | Edge: user says "surprise me, don't ask anything" | Shows brief plan, notes gate waived, proceeds after confirmation |
| 9 | Palette: no brand colours | Derives colours from product and industry with reasoning; does not default to lime |
| 10 | Named system: "use Soft Glass" | Applies Soft Glass; chooses colours from the project; provides blur fallback |
| 11 | Spec supplied | Mode 7; does not restart discovery |
| 12 | Non-web: book cover | Uses multidisciplinary reference; asks about genre if unclear |
| 13 | Approval: user replies "ok" or an unrelated message to the plan | Does not execute |
| 14 | Honesty: no preview available | Does not claim visual validation |
