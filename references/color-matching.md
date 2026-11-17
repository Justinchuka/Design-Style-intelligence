# Colour Matching: how to choose colours for a project

Colours are chosen per project. The techniques in this skill (illumination, layering, restraint, accent discipline) work with almost any palette. Never default to a favourite colour.

## Step 1: Read the project

Collect: existing brand colours and logo; industry; audience; emotional goal (trust, energy, calm, luxury, playfulness); competitors' colour conventions; any colour the user said is mandatory or banned.

## Step 2: Choose a strategy

| Strategy | When | Action |
|---|---|---|
| Keep | Strong, distinctive brand palette | Preserve brand hues; improve how they are applied |
| Refine | Brand palette is sound but harsh or flat | Adjust saturation/lightness, add tonal steps, keep hue identity |
| Derive | No brand palette or a weak one | Build from industry and emotion (below) |
| Replace | User wants a new identity and brand is not locked | Derive, and justify |

## Step 3: Industry and emotion starting points (heuristics, not rules)

| Intent | Typical hue families | Notes |
|---|---|---|
| Trust, finance, security | Deep blue, teal, graphite; restrained green for gains | Low saturation, high clarity |
| Growth, health, sustainability | Green, mint, warm sand | Avoid neon unless tech-forward |
| Energy, creator, youth | Orange, coral, vivid yellow, electric blue | Use blocks sparingly or boldly depending on system |
| Luxury, editorial | Black, ivory, bronze, burgundy | Accent very small |
| AI, developer, futuristic | Near-black with one luminous accent (lime, cyan, violet, amber) | Accent under ~3% of surface |
| Hospitality, craft, lifestyle | Terracotta, olive, clay, cream | Warm neutrals carry the design |
| Education, community | Friendly blue, green, warm yellow | High legibility first |

Break these when the product justifies it. Say why.

## Step 4: Build role-based tokens

Define roles, then assign values:

| Role | Purpose |
|---|---|
| bg-base, bg-raised | Page and section backgrounds |
| surface-1, surface-2, surface-3 | Card, elevated, interactive layers |
| border-subtle, border-strong | Dividers and card edges |
| text-primary, text-secondary, text-muted, text-disabled | Four text tiers |
| accent (signature) | Primary actions, active states, highlights |
| accent-soft | Low-opacity version for glows, tints, ghost elements |
| secondary accent (optional) | Only when content needs a second signal |
| semantic: success, warning, danger, info | Status, kept separate from brand accent |

Derive tonal steps with lightness shifts of the same hue family rather than adding new hues. Use opacity for secondary emphasis.

## Step 5: Distribution

Starting guide for dark systems: 85-90% neutral surfaces, 8-12% typography and secondary elements, 1-3% accent. Light systems: 80-90% neutral, accent 3-8%. Bold systems (Monolith, Swiss Signal) may run higher. Reserve the strongest contrast for the most important action.

## Step 6: Per-card identities

When a set of cards each needs its own accent (pricing tiers, feature grids): choose from the brand palette using analogous neighbours, a split-complementary pair, or tints of one hue at different temperatures. Keep saturation and lightness consistent across the set so none dominates by accident. Never assign random hues.

## Step 7: Verify

- Text contrast: aim for WCAG AA (4.5:1 body, 3:1 large text and UI parts).
- Accent-on-surface and button-text-on-accent contrast.
- Gradient and glow areas must not reduce legibility of foreground content.
- Colour is never the only carrier of meaning (add icon, label or pattern).
- Check the palette on the darkest and lightest surface it will touch.

## Worked example (illustrative only)

Dark AI tool, no brand palette: base #0D0D0D, surfaces #151515-#222222, borders #292929, text #F2F2F0 / #A0A0A0 / #777777, signature accent neon lime #DDFF00 at under 3%. A different product (a wellness app) would use the same layering and restraint with a warm sage accent on soft charcoal or a cream base. The technique is constant; the colour is chosen.
