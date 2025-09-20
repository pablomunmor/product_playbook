# Product Requirements Document (PRD) – Product Manager's Playbook

## Target Users
- **New PMs:** Learn role, competencies, lifecycle, and guardrails.
- **Experienced PMs:** Quickly access frameworks, prioritization, and OKRs.
- **Leaders:** Align team practices across orgs.

## Scope
### In-Scope
- Single HTML/JS/CSS file.
- LocalStorage persistence for edits.
- Screenshot export (PNG).
- Interactive lifecycle diagram (horizontal timeline).
- Editable templates with prefilled content.
- Auto-calculation for prioritization framework.
- Inline reset (per-template + global).
- Reference sections with curated external links.

### Out-of-Scope
- Multi-user collaboration.
- Backend storage or authentication.
- AI-driven personalization.

## Design & Theme
- **Style:** Nike-inspired minimalism.
- **Colors:** Marine Blue `#001F3F`, White `#FFFFFF`, light gray/blue accents.
- **Typography:** Inter (Google Fonts).
- **Layout:** Sticky sidebar navigation + scrollable cards.
- **Cards:** Rounded corners, shadows, clear headers.

## Functional Requirements
- Editable templates with **plain text bodies** and **styled headers**.
- LocalStorage persistence for all inputs.
- Reset buttons with inline confirmation (not browser popups).
- Screenshot export per card (PNG auto-download with filename `TemplateName.png`).
- Lifecycle diagram: horizontal timeline with clickable dots (expandable text).
- Prioritization framework: dropdowns 1–4, auto-weighted scoring.
- Reference bullets in-context for relevant external guides.

## Non-Functional Requirements
- Lightweight (<2MB).
- Runs offline in modern browsers (Chrome, Safari, Edge).
- Works when hosted on GitHub Pages.
- Keyboard/tab accessible navigation.

## Success Criteria
- **Ease of use:** PMs can edit templates without training.
- **Educational clarity:** Explanations are scannable and paired with examples.
- **Consistency:** One best framework per stage, no duplication.
- **Practicality:** Outputs can be used immediately in Miro/Confluence/decks.
