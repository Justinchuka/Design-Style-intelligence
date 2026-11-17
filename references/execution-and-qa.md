# Execution and Quality Assurance

## Execution order (after the plan is confirmed)

1. Define design tokens (colour roles, type scale, spacing, radii, shadows, motion) in the project's existing styling method (CSS variables, Tailwind theme, theme file).
2. Load fonts with a fallback stack; do not rely on a font you cannot load.
3. Redesign shared components: nav, buttons, inputs, cards, modals, tables.
4. Redesign sections and layouts, then every relevant page, not just the homepage.
5. Add assets only when they serve a purpose; never fabricate assets that misrepresent the product.
6. Add states and motion: hover, focus, active, disabled, loading, empty, error.
7. Responsive pass across large desktop, laptop, tablet, mobile.

## Safeguards

Do not rewrite backend logic, break integrations, remove working functionality, delete content, replace real data with decoration, add unnecessary dependencies, or overwrite unrelated work. Reuse the existing stack and conventions. If the frontend structure blocks the design, improve it without altering business logic.

## Accessibility

Contrast AA, visible focus states, adequate touch targets, reduced-motion respect, decorative layers hidden from assistive tech, colour never the only signal.

## Refinement loop

INSPECT, IDENTIFY, CORRECT, RE-INSPECT. Repeat until acceptable or blocked by a real limitation.

Checklist:

| Area | Check |
|---|---|
| Coherence | Sections feel related; tokens used consistently |
| Composition | Balanced, aligned, rhythm varied, no awkward gaps or repetition |
| Components | Buttons consistent; forms polished; tables/dashboards readable; states complete |
| Responsive | No horizontal overflow, clipping, overlap; stacks sensibly |
| Usability | Primary action obvious; text readable; contrast sufficient |
| Technical | Interactions work; images load; no layout errors or console errors where inspectable |

If you cannot render the result, say so and hand the user this checklist to run manually. Never state that something was tested if it was not.

## Completion report

Product understanding; visual transformation; design decisions (system, colour strategy, type); areas transformed; quality issues found and fixed; validation actually performed; outstanding limitations with genuine reasons. Do not report completion if only a few styles changed.
