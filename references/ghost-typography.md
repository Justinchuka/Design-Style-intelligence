# Ghost Typography, Faded Watermarks and Translucent Decorative Layers

Use subtle background typography and faded artwork inside selected cards to add depth. Applied to Level 2 and 3 components, never everywhere.

## Ghost typography

Oversized or partially visible background text used as decoration.
- Extremely low opacity: roughly 5-18% depending on background contrast.
- Muted, desaturated colour; tonal blending with the surface.
- Placed behind primary content; partly clipped by the card edge or extending beyond it.
- Positions: near the bottom, upper corners, or behind the main content.
- Content: product names, category labels, short identifiers, or abstract letterforms.
- Optional subtle blur or a fade-out mask so text gradually disappears.
- It must read as a watermark embedded in the surface, not another heading. Mark it decorative and hidden from assistive technology (aria-hidden, pointer-events none).

## Translucent decorative artwork

Transparent geometric outlines, faded coloured shapes, oversized ring/circle patterns, abstract type, partially visible illustrations, softly lit objects. Use translucent colours, not solid opaque fills; thin strokes; allow cropping at card edges.

## Layer model

| Layer | Content |
|---|---|
| 1 | Dark (or neutral) foundation surface |
| 2 | Atmospheric radial colour illumination |
| 3 | Ghost typography and translucent decorative artwork |
| 4 | Subtle edge highlights and surface details |
| 5 | Foreground content: icons, headings, text, metrics, buttons |

Layers 2-4 always sit behind layer 5.

## Variation rule

Do not repeat the same watermark on every card. Vary position, scale, opacity, cropping and combination: one card with faded text at the bottom, another with a large translucent shape in the upper corner, another with both, some with neither. The result should feel art-directed, not stamped.

## Implementation notes

- Implement with absolutely positioned pseudo-elements or background elements inside an `overflow: hidden` card.
- Use `user-select: none`, `pointer-events: none`, `z-index` below content.
- Use `clamp()` sizes so ghost text scales; check mobile for clipping that hides the whole word or causes horizontal overflow.
- Verify foreground contrast with the ghost layer present.
- Provide a reduced-motion-safe version if any layer animates.
