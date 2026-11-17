# Soft Glass (layered translucency)

**Philosophy:** gentle, airy depth. Frosted layers over soft colour fields feel light and modern. Works in light or dark.
**Best for:** consumer and mobile apps, wellness, lifestyle fintech, onboarding flows.

## Colour-role logic
- A calm, low-contrast background field with a soft, large blurred colour wash (one or two harmonious hues from the brand, low saturation).
- Glass surfaces: translucent white (light mode) or translucent dark (dark mode) at 6-18% opacity with a 1px light edge.
- Accent: clear and friendly, used for primary actions and active states.
- Text stays high contrast against the glass; test over the busiest part of the wash.

## Typography
Rounded or humanist sans, medium weights, comfortable sizes, friendly but not childish.

## Surfaces and cards
Radius 20-28px; backdrop blur used on a few key layers (nav, modal, hero card), not everywhere; soft long shadows; inner highlight on top edge.

## Layout
Stacked, overlapping layers, floating cards, generous padding, thumb-friendly targets on mobile.

## Motion
Soft springs on sheets and cards, subtle parallax only between layers, reduced-motion fallback.

## Avoid
Blurring everything, low-contrast text on glass, busy backgrounds behind text, heavy performance cost on low-end devices (provide a solid fallback).

## Quick start
Choose background wash; define two glass levels; apply blur to nav and one hero card; test contrast and a no-blur fallback.
