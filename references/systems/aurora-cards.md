# Aurora Cards (dark cards illuminated from within)

**Philosophy:** cards read as dark physical surfaces lit by coloured ambient light, not as coloured panels.
**Best for:** pricing tables, feature grids, dashboard highlights, product showcases.

## Colour-role logic
- Foundation is a deep neutral; colour appears only as illumination near the top of each card.
- Each card may have its own accent identity, derived from the brand palette (analogous or split-complementary; see `color-matching.md` step 6). Equal saturation and lightness across the set.
- CTA uses the card's accent as a solid fill with dark or high-contrast text.

## Surface recipe
1. Dark base surface, radius about 14-18px, thin low-contrast border.
2. 2-3 radial gradients of different size, position and opacity near upper-left, upper-right or upper-centre.
3. Fade colour out by mid-card; lower content area stays dark.
4. Faint dark linear gradient for depth; soft ambient shadow.
5. Optional coloured border glow near lit corners; subtle edge highlight.
6. Optional translucent geometry or ghost type, varied per card (see `ghost-typography.md`).

## Typography and content
Bright primary text, muted descriptions, strong numeric hierarchy for prices and metrics, consistent spacing between title, description, features and action.

## Intensity
Level 2 for feature cards, level 3 for pricing; the featured plan gets slightly stronger light.

## Motion
Hover: slightly stronger glow, border visibility, 2-4px lift, smooth CTA transition.

## Avoid
Filling the card with saturated colour; random hues; glow that reduces text legibility; identical decoration on every card; heavy blur on all cards.

## Quick start
Build one card with the recipe, extract it as a component with an accent variable, then instantiate per card with different accent and decoration placement.
