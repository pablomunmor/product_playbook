# Technical Specification – Product Manager's Playbook

## Architecture
- **Single-file HTML** (main.html).
- Vanilla JS for persistence, scoring, screenshot export, reset logic.
- [html2canvas](https://html2canvas.hertzen.com/) for PNG export.

## Data Model
- LocalStorage key format:
  `PMPlaybook.[Phase].[TemplateName].[Field]`

- Prioritization Framework formula:
Score = (Opp * 0.35) + (Cust * 0.20) + (Feas * 0.10) + (Strat * 0.35)

markdown
Copy code

## Scoring Tables
**Opportunity Value (35%)**
- 1 = < $100K  
- 1.5 = $100K–$500K  
- 2 = $500K–$1M  
- 2.5 = $1M–$1.5M  
- 3 = $1.5M–$2.5M  
- 3.5 = $2.5M–$3.5M  
- 4 = > $3.5M  

**Operational Value**
- 1 = negligible (<$1M savings)  
- 2 = moderate ($1M–$3M savings)  
- 3 = significant ($3M–$5M savings)  
- 4 = very high (> $5M savings)  

**Customer Value (20%)**
- 1 = negligible impact  
- 2 = moderate improvement  
- 3 = strong alignment + high desirability  
- 4 = very high desirability and reach  

**Feasibility Value (10%)**
- 0 = no available tech, no confidence  
- 1 = new tech/complex effort, low confidence  
- 2 = significant enhancements, low–medium confidence  
- 3 = moderate enhancements, medium–high confidence  
- 4 = existing tech, high confidence  

**Strategic Value (35%)**
- 1 = negligible impact  
- 2 = measurable contribution, somewhat foundational  
- 3 = significant, foundational unlocks  
- 4 = critical, measurable contribution, foundational unlock  

## Components
1. **Intro Section**
 - Title, What is a PM, Core competencies.
 - Interactive lifecycle diagram (horizontal timeline).

2. **Phases**
 - **Definition**: Vision & Strategy, PR/FAQ, 12-Month Strategy, Roadmaps.
 - **Discovery**: Lean Canvas, Hypotheses, Experiments, Idea Grid, Actor–Outcome Mapping, Discovery Sprint Guide.
 - **Delivery**: Prioritization Framework (auto-scoring), RACI, OKRs, Roadmap & Dashboard.
 - **Learning**: KPI Dashboard, UX Checklist, Continuous Learning Log.

3. **Template Cards**
 - Card structure:
   - What this is
   - Why it’s helpful
   - When to use
   - How to use
   - Done right looks like
   - Common pitfalls
   - Editable example (LocalStorage + Reset + Export)

4. **Global Controls**
 - Sidebar nav with phase anchors.
 - Global reset button with inline confirmation.
 - Global help section for “how to screenshot”.

## Interactivity
- **Lifecycle Diagram:** SVG/HTML horizontal timeline with clickable dots (expand → show definition, scroll to phase).
- **Editable Templates:** Inputs stored in LocalStorage.
- **Reset:** Inline confirmation banner inside card (“Are you sure? [Yes] [Cancel]”).
- **Screenshot:** `html2canvas` captures the card div, saves automatically as PNG (`TemplateName.png`).
- **Prioritization:** Dropdown inputs (1–4), weighted auto-calculation, live-updating score.