# Hiring Analysis: Patient Scheduling Solution

**Analysis Period:** October - December 2025
**Repositories Analyzed:**
- https://github.com/Precision-Medical-Group/patient-scheduling-solution
- https://github.com/Precision-Medical-Group/pss-client-issues

---

## Executive Summary

This analysis examines 3 months of development work to inform hiring decisions. A significant finding is that **~20% of development work was AI-generated**, which fundamentally changes the profile of an ideal hire.

---

## Work Analysis

### Contributor Breakdown

| Contributor | Commits | Percentage |
|-------------|---------|------------|
| Eric Halsey | 442 | 56% |
| Codex Agent (AI) | 108 | 14% |
| GitHub Action (automated) | 98 | 12% |
| Your Name | 89 | 11% |
| Copilot (AI) | 48 | 6% |

**Key Insight:** ~156 AI-generated commits out of ~690 non-automated commits = **20% AI contribution rate**

### Merged Pull Requests

| Author | Merged PRs |
|--------|------------|
| ehalsey | 256 |
| copilot-swe-agent | 44 |

---

## Engineering Metrics (LinearB-Style Analysis)

### Cycle Time

| Metric | Value | Assessment |
|--------|-------|------------|
| **Median Cycle Time** | 17 minutes | Excellent |
| **Average Cycle Time** | 3.7 hours | Good |
| **P75 Cycle Time** | 1.3 hours | Excellent |
| **P90 Cycle Time** | 4.7 hours | Good |
| **Max Cycle Time** | 205 hours | Outliers present |

### Cycle Time Distribution

| Time Range | PRs | Percentage |
|------------|-----|------------|
| Under 1 hour | 214 | 71% |
| 1-4 hours | 46 | 15% |
| 4-24 hours | 32 | 11% |
| Over 24 hours | 8 | 3% |

**Assessment:** Extremely fast cycle times. 71% of PRs merged within 1 hour indicates streamlined review process (likely due to single contributor + AI assistance).

### PR Size Distribution

| Size Category | Lines Changed | Count | Percentage |
|---------------|---------------|-------|------------|
| XS | < 10 | 30 | 10% |
| S | 10-100 | 87 | 29% |
| M | 100-500 | 77 | 26% |
| L | 500-1000 | 37 | 12% |
| XL | > 1000 | 69 | 23% |

**Assessment:** High proportion of XL PRs (23%) indicates some large feature work. Consider breaking down large PRs for better reviewability.

### Code Throughput

| Metric | Value |
|--------|-------|
| **Total PRs Merged** | 300 |
| **Total Additions** | 333,876 lines |
| **Total Deletions** | 70,749 lines |
| **Net Code Change** | +263,127 lines |
| **Avg Additions/PR** | 1,112 lines |
| **Avg Deletions/PR** | 235 lines |
| **Avg Files Changed/PR** | 14 files |
| **Single-File PRs** | 71 (24%) |

### Deployment Frequency (DORA Metric)

| Environment | Deployments | Frequency |
|-------------|-------------|-----------|
| DEV | 695 builds | ~7.5/day |
| UAT | Multiple releases | Weekly |
| PROD | ~10 releases | Bi-weekly |

**Top Workflow Runs (Q4 2025):**

| Workflow | Successful Runs |
|----------|-----------------|
| Build and Test PSS.UI | 695 |
| Environment Version Check | 506 |
| SMS MVP Automated Testing | 233 |
| Build PSS.API (Automated) | 183 |
| Coordinated Release | 84 |
| Deploy PSS.UI | 81 |
| Cypress Tests | 57 |
| Deploy Database Schema | 52 |

### AI Coding Agent Activity

| Workflow | Runs |
|----------|------|
| Running Copilot coding agent | 36 |
| Running Copilot | 18 |
| Copilot code review | 4 |
| Various "Addressing comment on PR" | 15+ |

### Benchmarking Against Industry

Based on LinearB's 2025 Engineering Benchmarks (8.1M+ PRs from 4,800 teams):

| Metric | This Repo | Industry Median | Assessment |
|--------|-----------|-----------------|------------|
| Cycle Time (Median) | 17 min | 2.5 hours | Top 10% |
| PR Size (Avg) | 1,347 lines | 200-400 lines | Above average (too large) |
| Deployment Frequency | Bi-weekly | Weekly | Average |
| PRs/Week | ~25 | Varies | High velocity |

---

## Technology Stack

### Primary Technologies

| Layer | Technology | Codebase Size |
|-------|------------|---------------|
| Frontend | React + TypeScript | 5.1 MB |
| Backend | Node.js, GraphQL (DAB) | - |
| Database | SQL Server + T-SQL | 2.7 MB |
| Infrastructure | Azure (Bicep) | 569 KB |
| CI/CD | GitHub Actions, Shell/PowerShell | 764 KB |

### Integrations & Services
- **Power BI** - Embedded dashboards with Row-Level Security
- **ConfigCat** - Feature flag management
- **Application Insights** - Telemetry and monitoring
- **SMS Provider** - Patient notifications
- **Azure WebPubSub** - Real-time updates
- **Azure Functions** - Serverless compute

---

## Types of Work Completed (Q4 2025)

### 1. SMS System Implementation
- Phased production rollout with feature flags
- Multi-language templates (English, Spanish)
- Queue management interface
- Patient-level debounce for reattempts
- Auto-refresh configuration without API restart
- Permanent failure handling

### 2. Power BI Integration
- Scheduler Dashboard reports
- Embed token generation with effective identity
- Row-Level Security (RLS) implementation

### 3. Performance Optimization
- React component re-renders reduced from 500+ to ~11
- Stored procedure optimization (sp_GetPatientChatterComprehensive)
- Database query tuning

### 4. DevOps & Infrastructure
- Data sync workflow refactoring into modular shell scripts
- GitHub Actions workflow fixes (ghost runs, dispatch issues)
- Environment-specific configuration preservation
- Database sync with settings protection

### 5. UI/UX Improvements
- GUID search and partial matching (5+ hex characters)
- ISO 8601 date format support
- Keyboard modifier navigation (ctrl+click, shift+click)
- In-app bug reporting with Application Insights

### 6. Database Development
- Complex stored procedures
- Trigger management (deadlock resolution)
- Transaction handling for DAB compatibility
- Idempotent migration scripts

---

## Hiring Recommendations

### Ideal Candidate Profile: "AI-Augmented Full-Stack Engineer"

Given the high AI contribution rate, the ideal hire is someone who can **orchestrate and validate AI-generated work** rather than write everything from scratch.

### Must-Have Technical Skills

| Skill | Priority | Rationale |
|-------|----------|-----------|
| TypeScript + React | Critical | Core frontend technology |
| SQL Server / T-SQL | Critical | Significant stored procedure work; AI struggles here |
| Azure Cloud | High | Infrastructure, Functions, WebPubSub, App Insights |
| Git / GitHub Actions | High | DevOps workflow management |
| Code Review | Critical | 80%+ of work involves reviewing AI output |

### Critical Soft Skills

1. **Prompt Engineering** - Ability to effectively direct AI coding tools
2. **Systems Thinking** - Understanding how components connect across the stack
3. **Quality Judgment** - Knowing when AI output is production-ready vs. needs refinement
4. **Documentation Mindset** - AI agents rely heavily on clear context and specifications
5. **Adaptability** - Comfortable with rapidly evolving AI tooling

### What NOT to Prioritize

- Deep specialization in one area (generalist > specialist for this role)
- Years of experience (adaptability matters more than tenure)
- Algorithm/data structure expertise (AI handles routine implementations)
- Computer science degree (practical skills matter more)

---

## Recommended Job Titles

- AI-Augmented Software Engineer
- Full-Stack Developer (AI-Assisted Development)
- Technical Lead - AI-First Development
- Software Engineer - Human-AI Collaboration

---

## Interview Strategy

### 1. Code Review Exercise
Present AI-generated code samples and ask candidates to:
- Identify bugs, security issues, or anti-patterns
- Suggest improvements
- Explain what they would accept vs. reject

### 2. Requirements Decomposition
Give an ambiguous feature request and evaluate:
- How they break it into AI-friendly tasks
- What clarifying questions they ask
- How they structure prompts/instructions

### 3. Technical Assessment

| Area | Assessment Method |
|------|-------------------|
| T-SQL | Write/debug a stored procedure (AI struggles here) |
| React | Review and refactor a component |
| Azure | Discuss architecture decisions |
| DevOps | Troubleshoot a failing GitHub Action |

### 4. AI Tool Proficiency
- Which AI coding tools have they used?
- How do they verify AI-generated code?
- What's their process for iterating on AI output?

---

## Alternative Hiring Strategy

Given the 20% AI contribution rate, consider:

### Option A: Senior "AI Orchestrator"
- Experienced developer comfortable directing AI
- Higher salary, but handles complex architectural decisions
- Best for: maintaining quality and strategic direction

### Option B: Junior + AI Tools
- Less experienced developer at lower cost
- Proficient with AI tools for day-to-day work
- Senior oversight for complex decisions
- Best for: maximizing cost efficiency

### Recommendation
**Option A** is recommended given the healthcare domain complexity and production criticality of the system.

---

## Appendix: AI-Generated Work Examples

The following types of work were successfully completed by AI agents:

```
fix: Convert CreatedAt to Pacific time in Entered Report view
feat: Add patient-level debounce for reattempt SMS notifications
perf: Optimize sp_GetPatientChatterComprehensive to fix production timeouts
Add keyboard modifier support for navigation (ctrl+click, shift+click)
Add GUID search and primary key filtering to all List components
Feature: Auto-refresh SMS configuration without API restart
Add duplicate check on form submit to catch phone+DOB matches
chore: make all migration scripts idempotent
Preserve environment-specific SystemConfiguration during database sync
Add in-app bug reporting with Application Insights telemetry
```

This demonstrates AI capability across:
- Bug fixes
- Feature development
- Performance optimization
- UI/UX improvements
- Database work
- DevOps/infrastructure

---

*Analysis generated: January 1, 2026*
