# Work Hours Estimate: 2026-02-01 to 2026-02-20

**Author:** ehalsey  
**Timezone:** America/Los_Angeles  
**Parameters:** max gap = 120min, first-commit bonus = 30min  

---

## Summary

| Metric | Value |
|--------|-------|
| Total estimated hours | **56.9h** |
| Total commits | 106 |
| Total sessions | 29 |
| Active days | 15 |
| Avg hours/active day | 3.8h |

---

## Per-Repository Breakdown

| Repository | Hours | Commits | % of Time |
|------------|------:|--------:|----------:|
| ACTO-LLC/modern-accounting | 22.3 | 36 | 39.2% |
| MBC-ORG-EHR/frontoffice | 15.5 | 28 | 27.3% |
| ACTO-LLC/acto-infra | 4.5 | 5 | 8.0% |
| Bamert-Seed/bamert-shopify | 4.0 | 5 | 7.0% |
| ACTO-LLC/scale-sync | 2.7 | 5 | 4.8% |
| ACTO-LLC/pas-base | 1.8 | 5 | 3.1% |
| ACTO-LLC/pas-notifications | 1.1 | 4 | 2.0% |
| ACTO-LLC/PAS-Crutch | 1.1 | 7 | 1.9% |
| ACTO-LLC/mbc-pm | 1.0 | 2 | 1.8% |
| ACTO-LLC/teams-recording-splitter | 1.0 | 2 | 1.7% |
| ACTO-LLC/strategy-planning | 0.5 | 3 | 1.0% |
| ACTO-LLC/ma-medplum | 0.5 | 1 | 0.9% |
| ACTO-LLC/acto-audit-history-daily-job | 0.5 | 1 | 0.9% |
| ACTO-LLC/partner-research | 0.2 | 1 | 0.3% |
| ACTO-LLC/OpenRec | 0.1 | 1 | 0.3% |

---

## Daily Breakdown

| Date | Day | Hours | Sessions | Commits |
|------|-----|------:|---------:|--------:|
| 2026-02-01 | Sun | 6.1 | 2 | 12 |
| 2026-02-02 | Mon | 10.1 | 2 | 15 |
| 2026-02-03 | Tue | 9.8 | 3 | 11 |
| 2026-02-04 | Wed | 1.5 | 2 | 3 |
| 2026-02-05 | Thu | 1.0 | 2 | 2 |
| 2026-02-06 | Fri | 0.5 | 1 | 1 |
| 2026-02-07 | Sat | 3.8 | 1 | 13 |
| 2026-02-08 | Sun | 0.5 | 1 | 1 |
| 2026-02-10 | Tue | 3.4 | 2 | 6 |
| 2026-02-11 | Wed | 1.2 | 1 | 3 |
| 2026-02-12 | Thu | 2.4 | 2 | 8 |
| 2026-02-16 | Mon | 0.5 | 1 | 1 |
| 2026-02-17 | Tue | 5.1 | 4 | 12 |
| 2026-02-18 | Wed | 4.4 | 2 | 5 |
| 2026-02-19 | Thu | 6.6 | 3 | 13 |

---

## Session Detail

<details><summary>Session 1: 2026-02-01 11:27–12:25 (1.5h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 11:27 | modern-accounting | QBO MCP consolidation and migration tracking fixes (#351) |
| 11:45 | modern-accounting | fix: Add SourceSystem/SourceId to DAB entity mappings (#352) |
| 11:52 | modern-accounting | fix: Pass auth token to executeGetMigrationStatus DAB calls |
| 12:25 | modern-accounting | fix: Pass auth token to executeQboAnalyzeMigration (#353) |

</details>

<details><summary>Session 2: 2026-02-01 19:08–23:15 (4.6h, 8 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 19:08 | modern-accounting | feat: Add SourceSystem/SourceId columns for migration tracking |
| 20:17 | modern-accounting | debug: Add migration skip reason logging |
| 20:36 | modern-accounting | fix: Add pagination to QBO searchVendors and searchCustomers |
| 21:14 | modern-accounting | feat: Add DAB pagination config to prevent 100-record limit |
| 21:16 | modern-accounting | docs: Add pagination anti-pattern to CLAUDE.md |
| 22:12 | modern-accounting | fix: Add Plaid health check endpoint for service detection |
| 22:58 | modern-accounting | fix: Add Managed Identity auth to Plaid service for DAB calls |
| 23:15 | modern-accounting | fix: Use Service role for Plaid DAB calls |

</details>

<details><summary>Session 3: 2026-02-02 08:38–16:48 (8.7h, 11 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 08:38 | modern-accounting | docs: Add Plaid integration auth flow lessons learned |
| 09:30 | modern-accounting | feat: Add qbo_get_trial_balance tool for cutoff date migrations |
| 10:57 | modern-accounting | fix: Use glob patterns in sqlproj and add missing views (#359) |
| 12:02 | modern-accounting | fix: Enable change tracking and fix local dev setup |
| 13:05 | modern-accounting | fix: Remove orphaned DAB entities missing from database |
| 14:49 | acto-infra | Add Apollo.io cold outreach setup documentation |
| 14:50 | scale-sync | Replace local MCP server with @mwhesse/mcp-dataverse npm package (#11) |
| 14:55 | scale-sync | Fix dataflow reassigning Scale Transaction IDs on every refresh |
| 15:56 | modern-accounting | fix: Add role-based permissions to all DAB entities |
| 15:59 | modern-accounting | feat: Add DAB config validation to prevent permission lockouts |
| 16:48 | modern-accounting | fix: Filter bank accounts by Subtype not Type in PlaidConnections |

</details>

<details><summary>Session 4: 2026-02-02 21:23–22:21 (1.5h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 21:23 | modern-accounting | fix: Route transaction endpoints through chat-api with proper DAB headers (#367) |
| 21:32 | modern-accounting | Fix: Bank account dropdown empty on PlaidConnections page (#362) |
| 22:00 | modern-accounting | feat: Add QBO source tracking update endpoint |
| 22:21 | modern-accounting | fix: Correct QBO query result parsing in source tracking endpoint |

</details>

<details><summary>Session 5: 2026-02-03 00:26–00:52 (0.9h, 3 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 00:26 | modern-accounting | feat: Add QBO trial balance report tool and opening balance JE script |
| 00:49 | modern-accounting | feat: Add Plaid connection re-authentication flow |
| 00:52 | modern-accounting | chore: Add QBO invoice migration script |

</details>

<details><summary>Session 6: 2026-02-03 10:56–16:12 (5.8h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 10:56 | modern-accounting | feat: Add QBO data export feature for Milton (#375) (#376) |
| 12:52 | modern-accounting | security: Add authentication to all /api/qbo/* endpoints (#378) |
| 14:35 | modern-accounting | refactor: Replace hardcoded QBO entity lists with dynamic discovery (#380) (#381 |
| 16:12 | acto-infra | Add CLAUDE.md, document presence routing, update Graph permissions |

</details>

<details><summary>Session 7: 2026-02-03 21:43–00:19 (3.1h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 21:43 | modern-accounting | fix: Resolve production auth, routing, and OData errors (#383) |
| 22:26 | scale-sync | Add alternate key for Scale Transaction ID and make schema script idempotent |
| 00:18 | scale-sync | Add solution v1.0.0.5 exports with alternate key fix |
| 00:19 | scale-sync | Merge pull request #12 from ACTO-LLC/fix/issue-10-preserve-scale-transaction-ids |

</details>

<details><summary>Session 8: 2026-02-04 15:23–15:51 (1.0h, 2 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 15:23 | teams-recording-splitter | Add Mail.Send permission to M365 app setup script |
| 15:51 | teams-recording-splitter | Add Azure Monitor alert for polling job failures (#8) |

</details>

<details><summary>Session 9: 2026-02-04 21:15–21:15 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 21:15 | frontoffice | build: rebuild intake module with updated asset hashes |

</details>

<details><summary>Session 10: 2026-02-05 10:56–10:56 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 10:56 | pas-base | Merge pull request #83 from ACTO-LLC/issue-82-reorganize-nav-menu |

</details>

<details><summary>Session 11: 2026-02-05 16:32–16:32 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 16:32 | pas-notifications | Move chat input to top of panel for D365 form visibility (#9) |

</details>

<details><summary>Session 12: 2026-02-06 07:16–07:16 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 07:16 | ma-medplum | Add accounting engine specification (ARM - Accounting Resource Model) |

</details>

<details><summary>Session 13: 2026-02-07 10:32–13:48 (3.8h, 13 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 10:32 | frontoffice | docs: move on-prem deployment guide to docs/deployment/ |
| 11:09 | frontoffice | docs: clean up local dev credentials in CLAUDE.md files |
| 11:29 | frontoffice | Merge pull request #209 from MBC-ORG-EHR/feat/199-patient-dashboard-customizatio |
| 11:37 | OpenRec | Initial commit: OpenRec project documentation |
| 11:47 | partner-research | Initial commit: EHR partner research and AI-first EHR strategy |
| 12:13 | frontoffice | feat: release management with VERSION file and CI workflow (#210) (#211) |
| 12:30 | frontoffice | fix: remove npm cache and use npm install in release workflow |
| 12:43 | frontoffice | fix: include deploy-docker.sh in bash build package script |
| 13:00 | frontoffice | fix: add appointment_queue, clinical_documentation, dashboard_context to build |
| 13:06 | frontoffice | docs: add release management lessons learned (#210) |
| 13:14 | frontoffice | docs: executive status report February 7, 2026 |
| 13:29 | frontoffice | docs: update dev completion target to July 2026 |
| 13:48 | acto-infra | Add blocked sender domains documentation |

</details>

<details><summary>Session 14: 2026-02-08 10:50–10:50 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 10:50 | pas-notifications | Merge pull request #11 from ACTO-LLC/feature/guided-tour |

</details>

<details><summary>Session 15: 2026-02-10 08:42–10:13 (2.0h, 2 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 08:42 | acto-infra | Convert quentin@a-cto.co from alias to standalone mailbox |
| 10:13 | bamert-shopify | Investigate Sideoats Haskell order sync failure and add audit tooling |

</details>

<details><summary>Session 16: 2026-02-10 12:17–13:08 (1.3h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 12:17 | frontoffice | fix: add Clinical Documentation to Miscellaneous menu (#212) |
| 12:43 | bamert-shopify | Add audit log findings, affected orders list, and blast radius analysis |
| 13:01 | bamert-shopify | Add D365 quote cross-reference findings |
| 13:08 | frontoffice | Merge pull request #213 from MBC-ORG-EHR/fix/212-clinical-docs-menu |

</details>

<details><summary>Session 17: 2026-02-11 07:26–08:10 (1.2h, 3 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 07:26 | pas-base | Merge pull request #71 from ACTO-LLC/rigel-solutions |
| 08:08 | pas-base | Update Dataverse MCP setup guide for Claude Code CLI |
| 08:10 | pas-base | Add Dataverse MCP reference to CLAUDE.md |

</details>

<details><summary>Session 18: 2026-02-12 08:49–09:13 (0.9h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 08:49 | strategy-planning | docs: Add Communications & Meetings operations playbook |
| 08:50 | strategy-planning | Merge pull request #10 from ACTO-LLC/feature/update-azure-mcp-config |
| 08:52 | strategy-planning | Merge pull request #11 from ACTO-LLC/feature/add-m365-mcp-config |
| 09:13 | acto-infra | Add Azure cost review howto documentation |

</details>

<details><summary>Session 19: 2026-02-12 11:50–12:48 (1.5h, 4 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 11:50 | frontoffice | fix: update SCSR demo data and calendar sidebar scroll |
| 12:20 | mbc-pm | initial commit: extract PM content from frontoffice |
| 12:43 | modern-accounting | feat: Add Azure SQL DB backup/restore workflow (#385) |
| 12:48 | frontoffice | chore: extract PM content to mbc-pm repo (#216) |

</details>

<details><summary>Session 20: 2026-02-16 23:23–23:23 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 23:23 | modern-accounting | feat: Add code coverage infrastructure, DAB proxy buffer, and test fixes |

</details>

<details><summary>Session 21: 2026-02-17 07:55–08:29 (1.1h, 6 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 07:55 | mbc-pm | Add project context, scheduling email, and 1-on-1 meeting notes |
| 07:56 | frontoffice | added admd providers list |
| 08:03 | pas-notifications | Add CSV export and clickable D365 record links to Audience Preview |
| 08:04 | pas-base | Replace acto_smsnumber with acto_passmsfrom and acto_contactsmsnumber in Account |
| 08:05 | pas-notifications | Add real DataverseService, pagination, and migrate to acto_accountcontact entity |
| 08:29 | frontoffice | feat: add providers list CSV file |

</details>

<details><summary>Session 22: 2026-02-17 10:37–10:37 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 10:37 | frontoffice | feat: add ADMD reference data files |

</details>

<details><summary>Session 23: 2026-02-17 17:46–18:06 (0.8h, 2 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 17:46 | frontoffice | Fix intake coordinator issues: navigation, save fields, E2E refactor (#235) |
| 18:06 | frontoffice | fix: persist rxType, location, treatingLocation, and copay across save/load (#23 |

</details>

<details><summary>Session 24: 2026-02-17 22:13–00:28 (2.7h, 3 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 22:13 | acto-audit-history-daily-job | Update README.md (#11) |
| 23:45 | frontoffice | feat: title case dropdowns, real auto-fill, attorney management (#228, #232) (#2 |
| 00:28 | frontoffice | feat: E2E tests support remote OpenEMR instances (#237) |

</details>

<details><summary>Session 25: 2026-02-18 09:25–11:53 (3.0h, 3 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 09:25 | frontoffice | feat: dotenv-based E2E config and fix ICD10 code search (#238) |
| 10:39 | frontoffice | docs: add Patient Documents & File Management section to implementation guide |
| 11:53 | bamert-shopify | Investigate DBSync phantom product creation in D365 (#4) |

</details>

<details><summary>Session 26: 2026-02-18 17:38–18:32 (1.4h, 2 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 17:38 | bamert-shopify | Fix DBSync phantom product creation and clean up 23 phantom products (#4) |
| 18:32 | frontoffice | data: update providers list with locations, new staff, and role corrections |

</details>

<details><summary>Session 27: 2026-02-19 08:38–13:17 (5.2h, 10 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 08:38 | PAS-Crutch | fix: Handle semicolon-separated emails and add error resilience (#5) |
| 08:43 | PAS-Crutch | docs: Add partial send recovery and retry instructions to readme |
| 08:51 | PAS-Crutch | fix: Address Copilot review feedback on error handling and counters |
| 08:52 | PAS-Crutch | Merge pull request #6 from ACTO-LLC/fix/5-handle-semicolon-emails |
| 08:53 | PAS-Crutch | fix: Add scratch directory to .gitignore |
| 09:05 | PAS-Crutch | fix: Use server paths in Config.ps1 |
| 09:14 | PAS-Crutch | fix: Escape $email variable references in string interpolation |
| 11:07 | frontoffice | fix: SSN masking pattern blocks form submit (#245) |
| 12:17 | frontoffice | Fix acronym undo re-expansion + intake form improvements (#249) |
| 13:17 | frontoffice | feat: duplicate patient detection on intake form (#251) |

</details>

<details><summary>Session 28: 2026-02-19 15:56–15:56 (0.5h, 1 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 15:56 | modern-accounting | feat(#338): Add Puppeteer support for JavaScript-rendered websites (#339) |

</details>

<details><summary>Session 29: 2026-02-19 18:29–18:55 (0.9h, 2 commits)</summary>

| Time | Repository | Message |
|------|------------|---------|
| 18:29 | modern-accounting | feat: Add production environment support to health check script |
| 18:55 | modern-accounting | chore: Remove seed/demo data from production (migrations 034 & 036) |

</details>
