# Product Manager's Playbook

An interactive, self-contained tool for Product Managers.  
It combines **education** (frameworks, best practices, anti-patterns, references) with **practicality** (editable templates, auto-calculations, export options).  
Built as a single HTML/JS/CSS file that runs locally or on GitHub Pages.

---

## Objectives
- Standardize product frameworks across teams.
- Accelerate onboarding for new PMs.
- Provide a daily workspace for experienced PMs.
- Encourage continuous learning with embedded references.

---

## Scope
- **In scope:** Single-file HTML, LocalStorage persistence, screenshot export (PNG), interactive lifecycle diagram, automated prioritization scoring, reference sections.
- **Out of scope:** Multi-user collaboration, backend storage, authentication.

---

## Tech Stack
- HTML, CSS, vanilla JS  
- [Google Fonts: Inter](https://fonts.google.com/specimen/Inter)  
- [html2canvas](https://html2canvas.hertzen.com/) for screenshot export  

---

## Structure
- **Intro Section** – What is a PM, core competencies, lifecycle diagram  
- **Phase 1: Definition** – Vision, PR/FAQ, Strategy, Roadmaps  
- **Phase 2: Discovery** – Lean Product Canvas, Hypotheses, Experiments, Guardrails  
- **Phase 3: Delivery** – Prioritization, RACI, OKRs, Roadmaps  
- **Phase 4: Learning** – KPIs, UX Metrics, Continuous log  

Each template follows the **card format**:
- What this is  
- Why it’s helpful  
- When to use  
- How to use  
- Done right looks like  
- Common pitfalls  
- Editable example (with LocalStorage + export)  

---

## Running Locally
1. Clone repo:
   ```bash
   git clone https://github.com/your-org/product-managers-playbook.git
   cd product-managers-playbook
Open main.html in your browser.

Deployment (GitHub Pages)

Push to main branch.

In repo settings → Pages → Source = main + / (root).

Access at https://your-org.github.io/product-managers-playbook/.

Documentation

Business Requirements Document

Product Requirements Document

Technical Specification

Information Architecture

References

Product Discovery Guide – productstrategy.co

Product Strategy Frameworks – productstrategy.co

Synthesizing Insights – productstrategy.co

Product Objectives & Key Results – productstrategy.co

Lean Product Canvas – Jeff Gothelf

Hypothesis Prioritization Canvas – Jeff Gothelf

OKR Tracking Tool – Jeff Gothelf

7 Questions to Craft the Perfect Product Story – Jeff Gothelf

OKR and User Story Mapping – Jeff Gothelf

How to Create an OKR-Based Roadmap (video) – Jeff Gothelf

12 Icebreakers to Kick Off Your Next Zoom Meeting – Jeff Gothelf

Contribution Guidelines

Do not overwrite main.html.

Use a scratchpad file (scratch.html) for experiments.

PRs must include diffs, not full rewrites.


---

# 📄 docs/BRD.md

```markdown
# Business Requirements Document (BRD) – Product Manager's Playbook

## Objective
Build a **self-contained, interactive playbook** for product managers of all levels.  
It balances **education** (core principles, best practices, anti-patterns, references) with **practicality** (editable templates, auto-calculations, export options).  
It must function as both a **training resource** and a **day-to-day workbench**.

## Business Goals
- Standardize product management processes and frameworks across teams.
- Onboard new PMs faster by providing lifecycle education in one place.
- Equip experienced PMs with ready-to-use templates and scoring systems.
- Enable PMs to export/share outputs (Miro, Confluence, decks).
- Create a living tool that emphasizes continuous learning.

## Success Metrics
- **Adoption:** Number of PMs using the playbook weekly.
- **Retention:** % of PMs who reuse templates over multiple sessions.
- **Learning impact:** Reduced onboarding time, self-reported competency increases.
- **Practicality:** # of screenshots/exports used in workflows.