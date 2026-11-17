# Example Plans (illustrative, fictional products)

These show the expected behaviour of the confidence gate. The products are invented.

## Example 1: High confidence, no questions

**Request:** "Redesign my project's landing page to look more premium." The project is a Next.js site for "LedgerLoop", an invoicing tool for freelancers, with an existing blue logo.

**Gate result:** product High, audience High (freelancers, from copy), brand Medium (logo blue found, palette unspecified), scope High, direction Medium, intensity Medium. No Low, so no questions.

**Plan shown (abridged):**
1. Found: invoicing SaaS; pages: home, pricing, login; Tailwind; inspected code only, no rendered preview.
2. Diagnosis: flat white sections repeat the same three-card row; pricing hierarchy is weak; accent blue used on every link.
3. Colour strategy: Refine. Keep the logo blue as the signature accent, deepen it, add a neutral ladder; accent under 5%.
4. Direction: Paper & Ink foundation with Swiss Signal grid in the pricing comparison; serif display plus sans.
5. Changes: hero (typography-led), features (alternate split and editorial rows), pricing (comparable cards, stronger featured plan), footer.
6. Preserve: routes, copy, auth, billing logic.
7. Assumptions: blue is not mandatory in exact shade; tablet and mobile checked from code only.
8. "Shall I proceed with this plan, or adjust anything first?"

## Example 2: Low confidence, targeted questions first

**Request:** "Make my app look modern." Only three screenshots, no code. Screens show a dashboard of unlabelled charts.

**Gate result:** product Low (cannot tell what the data means), audience Low, brand Low (unclear if the teal is a logo colour), scope Medium, direction Low, intensity Low.

**Questions asked (max 3):**
1. What is this dashboard used for, and by whom?
2. Is the teal a fixed brand colour or open to change?
3. Do you want a polish or a full redesign?

After answers, the full plan is presented with the same eight parts and confirmation line.

## Example 3: Prescriptive spec (Mode 7)

**Request:** the user pastes a full design system and says "apply this". Skip discovery; confirm scope in one line ("all marketing pages, not the admin area, correct?") only if unclear, then present a short plan and proceed after confirmation.
