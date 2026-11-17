# Confidence Gate

Purpose: decide, after inspection, whether to ask questions before planning. The goal is a design the user would have chosen themselves, with the fewest possible interruptions.

## Step 1: Rate understanding

| Dimension | High | Medium | Low |
|---|---|---|---|
| Product and purpose | Obvious from code/content/screens | Probable but unverified | Cannot tell what it does or sells |
| Audience | Stated or evident | Inferable from industry | Unknown and it changes tone (e.g. B2B vs kids) |
| Brand constraints | Brand assets or palette supplied/found | Some brand cues | Unclear what is fixed (logo colour? existing palette mandatory?) |
| Scope and access | Pages, files, tools known | Mostly known | Unclear what to touch or what access exists |
| Direction | Reference, design spec or clear brief | User hints at a mood | No signal, and multiple valid directions |
| Intensity | Stated ("polish" vs "reimagine") | Implied | Unclear, and outcomes differ greatly |

A Low only counts if the answer would change the design. If you can make a safe assumption, rate it Medium and state the assumption.

## Step 2: Branch

| Outcome | Action |
|---|---|
| No Low | Skip questions. Present plan. |
| One or more Low that matter | Ask 1-3 questions covering only those items. Then present plan. |
| User delegated ("you decide") | Treat related dimensions as High; decide and justify in the plan. |
| User supplied a full design spec | Mode 7: skip discovery, confirm scope only if unclear. |

## Question rules

- Maximum 3. Ask them together in one message, each answerable in a few words. Offer 2-4 options where possible plus "you decide".
- Never ask what inspection can answer. Never ask about font, palette, or light/dark unless a brand constraint or strong preference is at stake.
- Good questions: "Is the green in your logo mandatory, or can the palette evolve?" "Is this for investors or end customers?" "Should I touch the checkout flow or only marketing pages?"
- Bad questions: "Which colours do you like?" "Do you prefer rounded corners?"

## Step 3: The plan (always shown before executing)

Use this structure, each part short:

1. **What I found:** product, audience, how it works (state what you actually inspected).
2. **Diagnosis:** the 3-5 most consequential visual weaknesses and what already works.
3. **Colour strategy:** keep / refine / derive, with the reasoning and the role-based palette.
4. **Direction:** chosen system(s) and why; typography; composition approach; intensity level.
5. **Transformation plan:** real sections and components, what changes in each.
6. **Preserve:** what stays untouched.
7. **Assumptions:** every Medium item.
8. **Recommendation and confirm line:** "Shall I proceed with this plan, or adjust anything first?"

Then stop. Execution begins only after a clear yes ("proceed", "go ahead", "yes"). Silence or an unrelated reply is not approval. If the user adjusts, revise the plan and confirm again.

If the environment allows two directions (Mode 5), make them differ in philosophy and composition, not only colour.
