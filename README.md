# Styling Intelligence

**by Maveric**

An autonomous visual design and art-direction skill for AI assistants and AI builders. Point it at a website, app, dashboard or visual artifact and it inspects what exists, diagnoses what is weak, chooses colours and a design system that fit your product, shows you a plan, and then redesigns it with modern, premium visual techniques.

## What makes it different

- **Techniques over colours.** The upgrade is how colour, light, depth, type and space work together (layered surfaces, atmospheric illumination, ghost typography, accent discipline, composition). Colours are chosen for *your* product, never imposed.
- **It decides when to ask.** After inspecting, it rates its own understanding. If it understands, it goes straight to a plan. If something important is unclear, it asks up to three targeted questions first. Either way you confirm a plan before anything changes.
- **Eight named systems** you can request by name, blend, or have it invent a new one from.
- **Preserves function.** Logic, content, routes and data stay intact; appearance is what changes.

## Included systems

| System | Character | Good for |
|---|---|---|
| Nocturne | Dark, cinematic, one luminous accent | SaaS, AI, developer tools |
| Aurora Cards | Dark cards lit from within | Pricing, feature grids, dashboards |
| Ghostframe | Typography-led depth, watermarks | Agencies, portfolios, marketing |
| Paper & Ink | Warm editorial calm | Content, education, consulting |
| Swiss Signal | Strict grid, flat, one signal colour | Corporate, B2B, data |
| Soft Glass | Layered translucency | Consumer and mobile apps |
| Terracotta Studio | Warm, tactile, organic | Hospitality, lifestyle, e-commerce |
| Monolith | Neo-brutalist, bold blocks | Creator brands, startups |

## Folder structure

```
styling-intelligence/
├── SKILL.md                  core instructions
├── references/               gate, inspection, colour matching, art direction,
│                             components, card composition, ghost typography,
│                             execution and QA, non-web artifacts
│   └── systems/              the eight named systems and a selection guide
├── portable/                 single-file version for tools without skill folders
├── examples/  evals/  scripts/
├── README.md  LICENSE
```

## How to use it

**Tools that load skill folders:** place the `styling-intelligence` folder where your tool reads skills (for Claude, upload it as a skill in Settings or add it to your skills directory). Then ask, for example: "Restyle my site to look premium", "Apply the Aurora Cards system to my pricing section", or "Choose colours that fit my brand and redesign the hero".

**Any other AI builder or chat assistant (Cursor, Lovable, Bolt, v0, Replit, ChatGPT, Gemini and similar):** open `portable/styling-intelligence-prompt.md`, paste it as the system prompt, project rules or first message, then describe what you want styled. This is the recommended path where skill folders are not supported.

The instructions are written in tool-agnostic language. Wherever they say "inspect", the AI uses whatever it can access (code, a preview, screenshots, or your description) and should say which it had.

## What you can expect

1. A quick inspection and diagnosis.
2. Possibly up to three clarifying questions, only if they would change the design.
3. A written plan: what it found, colour strategy, chosen system, what changes, what stays. You confirm or adjust.
4. The redesign, then a review and a completion report stating what was actually checked.

## Limitations

- Quality depends on what the host tool can access. Without a live preview, rendered review is not possible and the AI should say so.
- Font and asset availability varies by tool; fallbacks are specified.
- Compatibility with specific builders has not been tested by the author; the usage notes above describe how to apply it, not a verified support matrix.
- The `evals/` prompts are provided for you to run; results are not included.

## Credits and licence

Created by Maveric. MIT licensed (see `LICENSE`).
