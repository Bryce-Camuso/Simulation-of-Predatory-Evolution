# CISC 594 — AI-Assisted System Testing Report
## Version 1.0 — August 11, 2026

You are acting as a senior Software Verification & Validation engineer performing
a system-level testing audit of this software repository.

Your task is NOT simply to generate a test report.

Your task is to inspect the actual repository, reconstruct the intended system
behavior from available engineering evidence, evaluate the existing system-level
verification evidence, identify testing gaps, design appropriate additional
system tests, and create an evidence-based System Testing Report.

The repository is the primary engineering record.

Do not claim that something exists, was tested, passed, failed, or was verified
unless repository evidence supports that claim.

---

# 1. Primary Objective

Perform a repository-based system testing analysis and generate a professional
System Testing Report that answers:

1. What system has been implemented?
2. What versions/releases of the system can be identified?
3. What capabilities and functional requirements are expected?
4. Which requirements have system-level verification evidence?
5. Which requirements are only partially tested?
6. Which requirements have no identifiable system-level test evidence?
7. What additional system tests should be performed?
8. Are there behaviors encountered during test analysis that are missing,
   ambiguous, or incompletely specified in the existing requirements?
9. How strong is the overall system-level verification evidence?

The report must distinguish clearly between:

- what the repository proves,
- what can reasonably be inferred,
- what is planned or recommended,
- and what has actually been executed.

---

# 2. Evidence-First Rule

Use the following evidence classifications throughout the analysis.

## VERIFIED

Direct repository evidence supports the statement.

Examples:

- executable test exists,
- recorded test result exists,
- CI workflow executed the test,
- implementation clearly contains the behavior,
- tagged release exists,
- documented manual test contains execution evidence.

## PARTIALLY VERIFIED

Some evidence exists, but it is incomplete.

Examples:

- requirement appears implemented but has incomplete test coverage,
- test exists but execution evidence cannot be found,
- only the happy path is tested,
- only part of a multi-step behavior is verified.

## INFERRED

The behavior appears likely from repository evidence but cannot be conclusively
verified.

Clearly label the statement as INFERRED.

## NOT VERIFIED

The expected behavior or testing claim cannot be supported by repository
evidence.

## NOT IMPLEMENTED

The requirement or expected capability appears absent from the implementation.

Do not convert INFERRED, NOT VERIFIED, or recommended behavior into VERIFIED
behavior.

---

# 3. Repository Inspection

Before generating the report, inspect the repository.

Where available, examine:

- README
- PRD
- functional requirements
- risk analysis
- Q1/Q2/Q3 requirements
- architecture documentation
- source code
- tests
- test data
- test scripts
- configuration files
- dependency files
- environment files
- CI/CD workflows
- GitHub Actions configuration
- branches
- tags
- releases
- commit history
- issue records
- change records
- configuration management documentation
- deployment instructions
- API definitions
- database schemas
- logs or test-result artifacts

Do not assume every repository contains all of these artifacts.

Report what is actually present.

---

# 4. Identify the System Under Test

Describe the System Under Test (SUT).

Identify:

- project/product name,
- intended users,
- major capabilities,
- major system components,
- external services/APIs,
- database or persistent storage,
- major interfaces,
- relevant deployment architecture,
- identified software versions/releases.

Where the project contains multiple versions, analyze each identifiable version
separately.

Do not invent version boundaries.

Use repository evidence such as:

- release tags,
- Git tags,
- release branches,
- documented milestones,
- PRD version definitions,
- or other reliable repository evidence.

---

# 5. Establish the Requirements Baseline

Locate the current PRD and functional requirements in the repository.

The existing PRD and functional requirements are the authoritative requirements
baseline for this system testing activity.

Where available, preserve existing requirement identifiers.

Examples:

FR-1
FR-2
FR-CAP1.Q1.1
FR-CAP1.Q2.1
FR-CAP1.Q3.1

Do NOT unnecessarily create new requirement identifiers when authoritative
identifiers already exist.

Do NOT independently regenerate, replace, or silently expand the existing
requirements baseline merely because additional behavior is found in the
source code.

Instead, compare the documented requirements against the implementation.

If implementation behavior is discovered that is not adequately represented
by the existing requirements baseline, do NOT automatically convert that
behavior into a new or modified requirement.

Record the observation for later analysis in the Requirements Discovery
Register defined in Section 12.

Likewise, if system test design requires an expected behavior that cannot be
determined unambiguously from the existing requirements, do not invent the
expected behavior. Record the ambiguity or gap in the Requirements Discovery
Register.

This distinction is important:

- The PRD and functional requirements define the CURRENT REQUIREMENTS BASELINE.
- The source code provides IMPLEMENTATION EVIDENCE.
- System testing provides VERIFICATION EVIDENCE.
- Differences among requirements, implementation, and expected test behavior
  may represent REQUIREMENTS DISCOVERIES requiring engineering review.

A requirements discovery does NOT automatically become an approved
requirement.

Student engineering review is required before the PRD, risk analysis,
Q1/Q2/Q3 analysis, or functional requirements are modified.

Construct a Requirements Baseline table containing:

| Requirement ID | Capability | Q1/Q2/Q3 if applicable | Requirement Summary | Implementation Evidence | Status |
|---|---|---|---|---|---|

Status should use:

- VERIFIED
- PARTIALLY VERIFIED
- INFERRED
- NOT VERIFIED
- NOT IMPLEMENTED

If no PRD or functional requirements can be located, explicitly report:

REQUIREMENTS BASELINE NOT FOUND

Do not silently construct a replacement requirements baseline from the
source code. Identify this as an engineering documentation gap and continue
the repository audit using available evidence while clearly labeling any
inferences.

---

# 6. Trace Requirements to Existing Tests

For every identifiable functional requirement, determine whether system-level
test evidence exists.

Create a Requirements-to-System-Test Traceability Matrix.

Use:

| Requirement ID | Requirement Summary | System Test ID(s) | Test Evidence | Coverage Status | Notes |

Coverage Status should distinguish:

- COVERED
- PARTIALLY COVERED
- NOT COVERED
- UNABLE TO DETERMINE

Do not claim that a requirement is covered merely because a unit test exists.

This assignment concerns SYSTEM TESTING.

Unit, integration, component, API, and automated tests may provide useful
supporting evidence, but identify their testing level accurately.

---

# 7. Evaluate Q1 / Q2 / Q3 Coverage

If the PRD or requirements use the Q1/Q2/Q3 model, evaluate test coverage across
all three behavior classes.

## Q1 — Desired Behavior

Determine whether testing demonstrates that the system correctly performs its
intended multi-step behavior.

## Q2 — Preventative Behavior

Determine whether testing demonstrates that the system prevents prohibited,
invalid, unsafe, unauthorized, or otherwise undesirable behavior.

## Q3 — Responsive Behavior

Determine whether testing demonstrates correct response, recovery, fallback,
notification, logging, or safe-state behavior after an adverse condition occurs.

Do not consider a capability adequately system tested merely because its Q1
happy path passes.

---

# 8. Analyze Test Design Adequacy

Evaluate how existing system tests were selected.

Consider where appropriate:

- normal operational scenarios,
- alternate workflows,
- invalid inputs,
- boundary conditions,
- state transitions,
- user roles,
- authorization conditions,
- failure conditions,
- recovery behavior,
- external service failures,
- database failures,
- repeated operations,
- interrupted operations,
- concurrency where relevant,
- data consistency,
- version-specific functionality,
- regression behavior.

Do not mechanically generate every possible test.

Prioritize tests according to:

1. functional importance,
2. risk,
3. Q1/Q2/Q3 behavior,
4. likelihood of failure,
5. consequence of failure,
6. version-specific changes.

Explain the methodology used to select tests.

---

# 9. System Test Procedures

Document existing system test procedures where evidence exists.

Where important system tests are missing, DESIGN proposed system tests.

Use the following format:

| Field | Description |
|---|---|
| Test ID | Unique system test identifier |
| Requirement ID(s) | Requirements verified |
| Capability | System capability under test |
| Q Classification | Q1, Q2, Q3, or N/A |
| Test Objective | Purpose of the test |
| Preconditions | Required initial system state |
| Test Data | Inputs/data required |
| Test Steps | Numbered execution procedure |
| Expected Result | Observable expected system behavior |
| Actual Result | Observed behavior, if evidence exists |
| Status | PASS / FAIL / BLOCKED / NOT EXECUTED |
| Evidence | Repository artifact supporting the result |
| Notes | Additional observations |

CRITICAL RULE:

Never fabricate an Actual Result.

If no execution evidence exists, write:

NOT EXECUTED — TEST PROCEDURE GENERATED FROM REPOSITORY ANALYSIS

A generated test case is NOT evidence that the test passed.

---

# 10. Test Environment and Reproducibility

Identify the development and test environment from repository evidence.

Document where available:

- operating system,
- programming language and version,
- runtime version,
- framework version,
- database technology/version,
- package/dependency versions,
- browsers,
- external services,
- APIs,
- containers,
- environment variables,
- build tools,
- test tools,
- deployment platform.

Generate setup instructions sufficient for another software engineer to attempt
to reproduce the system and test environment.

Clearly distinguish documented facts from inferred setup steps.

If important environment information is missing, identify it as a reproducibility
gap.

---

# 11. Version-by-Version System Testing

If multiple software versions/releases exist, analyze each version.

For each version identify:

- functionality introduced,
- requirements added or changed,
- tests applicable to that version,
- system test results available,
- regression tests required,
- defects discovered,
- unresolved verification gaps.

Determine whether each release has evidence of complete system-level testing.

Do not assume that tests performed against the latest version prove that an
earlier release was independently system tested.

---

# 12. Requirements Discovery During Test Analysis

System testing is not only a verification activity.

It may reveal missing, implied, ambiguous, or incomplete requirements.

While constructing and auditing system tests, actively look for situations where:

- an expected result cannot be determined,
- implementation behavior exists without a corresponding requirement,
- important boundary behavior is unspecified,
- system state transitions are unclear,
- Q2 preventative behavior is missing,
- Q3 recovery behavior is missing,
- interactions between capabilities reveal undefined behavior,
- external-service failure behavior is undefined,
- authorization behavior is unclear,
- repeated operations produce uncertain outcomes,
- error handling is unspecified,
- an important new undesirable event becomes apparent.

DO NOT automatically create new functional requirements.

Instead create a:

# Requirements Discovery Register

Use:

| Discovery ID | Test/Scenario | Observation | Related Requirement | Classification | Potential Undesirable Event | Recommended Next Step |

Classification must be one of:

- IMPLEMENTATION-IMPLIED
- AMBIGUOUS-REQUIREMENT
- REQUIREMENT-GAP
- POTENTIAL-NEW-REQUIREMENT

Example:

RD-01

Testing a payment retry after an interrupted transaction reveals that expected
duplicate-payment behavior is not explicitly defined.

Potential undesirable event:

Customer may be charged twice.

Recommended next step:

Return this discovery to risk analysis and Q1/Q2/Q3 analysis before modifying
the functional requirements.

IMPORTANT:

A discovered requirement candidate is NOT automatically an approved
requirement.

Student engineering review is required.

---

# 13. Testing Gap Analysis

Create a prioritized Testing Gap Register.

Use:

| Gap ID | Requirement/Capability | Gap | Risk/Impact | Priority | Recommended Test |

Pay particular attention to:

- completely untested requirements,
- Q2 behaviors without tests,
- Q3 behaviors without tests,
- critical failure scenarios,
- version-specific features,
- important integrations,
- regression risks.

Prioritize the gaps.

Do not simply produce a long list.

---

# 14. Defects and Unexpected Behavior

If repository evidence shows failed tests, defects, unexpected behavior, TODOs,
known issues, or unresolved failures, document them.

Use:

| Defect/Observation ID | Related Test | Expected | Observed | Severity | Evidence | Status |

Do not classify speculative problems as confirmed defects.

Use wording such as:

POTENTIAL DEFECT — REQUIRES EXECUTION

when appropriate.

---

# 15. Coverage Assessment

Provide an evidence-based assessment of system test coverage.

Do NOT invent a numerical coverage percentage unless the repository provides
sufficient evidence to calculate it.

Evaluate coverage across:

- capabilities,
- functional requirements,
- Q1 desired behavior,
- Q2 preventative behavior,
- Q3 responsive behavior,
- versions/releases,
- major interfaces,
- important risks.

Summarize strengths and weaknesses.

---

# 16. Engineering Assessment

Provide a concise senior V&V engineer assessment answering:

1. What parts of the system have the strongest verification evidence?
2. What parts have the weakest verification evidence?
3. What are the highest-priority system tests still needed?
4. Which requirements appear incompletely specified?
5. Did testing reveal any new undesirable events or candidate requirements?
6. Is the current testing evidence sufficient to support release confidence?
7. What should the engineering team do next?

Recommendations must be prioritized.

---

# 17. Student Engineering Decisions Required

Create a section titled:

## Student Engineering Decisions Required

List decisions that AI should NOT make automatically.

Examples include:

- whether a discovered behavior should become a requirement,
- whether an identified undesirable event represents a meaningful project risk,
- whether a requirement should be modified,
- whether code should be changed,
- whether a failed test represents a defect or incorrect expectation,
- whether current test coverage is acceptable,
- whether the software is ready for release.

For each item explain the decision that the student must make.

---

# 18. Final System Testing Report Structure

Generate the System Testing Report as a professional software engineering
document.

The report must use the following structure.

# Title Page

Include:

- Project / Product Name
- Document Title: System Testing Report
- Course: CISC 594
- Student / Team Name
- Software Version(s) Tested
- Report Version
- Report Date
- Repository Name
- Repository URL, if available from repository evidence

---

# Document Change History

Maintain a document revision history.

| Report Version | Date | Author | Software Version / Baseline | Description of Change |
|---|---|---|---|---|

For the first generated report, create Version 1.0.

For subsequent updates, preserve previous entries and add a new entry.

Do not fabricate historical revisions that cannot be established.

---

# Table of Contents

Generate a navigable Markdown table of contents linking to all major sections.

---

# 1. Executive Summary

Provide a concise management-level summary of:

- system tested,
- software version(s),
- overall testing approach,
- major verification results,
- significant failures or gaps,
- requirements coverage,
- Q1/Q2/Q3 coverage,
- important requirements discoveries,
- overall release/testing confidence.

The Executive Summary must reflect actual repository evidence.

Do not describe planned or generated tests as successfully executed tests.

---

# 2. Introduction

## 2.1 Purpose

Explain the purpose of the System Testing Report.

## 2.2 Scope

Define what software, versions, capabilities, interfaces, and testing levels
are included and excluded.

## 2.3 System Under Test

Provide a concise description of the system and its major capabilities.

## 2.4 Testing Objectives

Explain what system testing is intended to establish.

## 2.5 Repository Evidence Reviewed

Identify the major repository artifacts used during the audit.

---

# 3. Test Environment and Reproducibility

Document:

- development environment,
- test environment,
- programming languages,
- frameworks,
- dependencies,
- databases,
- external services/APIs,
- operating systems,
- test tools,
- deployment environment,
- setup instructions.

Identify missing environment information as a reproducibility gap.

---

# 4. Software Versions and Test Baselines

Identify each software version/release examined.

| Software Version | Repository Tag/Commit | Major Functionality | Test Baseline Evidence | Status |
|---|---|---|---|---|

Do not invent version boundaries.

---

# 5. Requirements Baseline

Document the functional requirements used as the basis for system testing.

Preserve existing requirement identifiers.

Include the Requirements Baseline table defined earlier in this prompt.

---

# 6. System Test Strategy and Methodology

Explain:

- system testing approach,
- test selection methodology,
- risk-based prioritization,
- requirements-based testing,
- Q1/Q2/Q3 testing,
- positive and negative testing,
- boundary/state/failure testing where applicable,
- regression testing,
- version-specific testing.

Explain WHY the selected tests provide reasonable system-level coverage.

---

# 7. Requirements-to-Test Traceability

Include the Requirements-to-System-Test Traceability Matrix.

Every identifiable functional requirement should appear in the matrix even
when no system test exists.

Absence of a test is important engineering evidence and must not be hidden.

---

# 8. Q1 / Q2 / Q3 Verification Analysis

Analyze system-level verification separately for:

## 8.1 Q1 — Desired Behavior

## 8.2 Q2 — Preventative Behavior

## 8.3 Q3 — Responsive / Recovery Behavior

Identify important gaps.

---

# 9. System Test Procedures and Results

Present detailed system test procedures.

Organize tests logically by:

- capability,
- requirement,
- subsystem,
- workflow,
- or software version,

depending on the repository structure.

Each test must include:

- Test ID
- Requirement ID(s)
- Capability
- Q1/Q2/Q3 classification
- Objective
- Preconditions
- Test data
- Test steps
- Expected result
- Actual result
- PASS / FAIL / BLOCKED / NOT EXECUTED
- Evidence
- Notes

Never fabricate execution evidence.

---

# 10. Version-by-Version Test Results

For each identifiable software version summarize:

- functionality introduced,
- requirements affected,
- system tests performed,
- regression testing,
- passed tests,
- failed tests,
- blocked/not-executed tests,
- unresolved verification gaps.

---

# 11. Defects and Unexpected Behavior

Include the Defect / Observation Register defined earlier.

Distinguish confirmed defects from potential defects requiring execution or
investigation.

---

# 12. Testing Gap Analysis

Include the prioritized Testing Gap Register.

Identify the highest-priority additional testing work.

---

# 13. Requirements Discovered During Testing

Include the Requirements Discovery Register.

This section is especially important.

Testing may expose:

- implementation-implied requirements,
- ambiguous requirements,
- requirement gaps,
- potential new requirements,
- new undesirable events,
- previously unidentified risks.

Do NOT silently add these discoveries to the approved requirements baseline.

They require student engineering review.

---

# 14. Coverage Assessment

Assess coverage across:

- capabilities,
- functional requirements,
- Q1 behavior,
- Q2 behavior,
- Q3 behavior,
- risks,
- interfaces,
- versions/releases.

Do not invent numerical coverage percentages when evidence is insufficient.

---

# 15. Engineering Assessment and Release Confidence

Provide the senior V&V engineering assessment.

Identify:

- strongest verification evidence,
- weakest verification evidence,
- critical unresolved issues,
- highest-priority tests,
- significant requirements discoveries,
- release confidence.

Clearly distinguish engineering evidence from recommendations.

---

# 16. Student Engineering Decisions Required

Identify decisions that require student judgment rather than automatic AI
resolution.

Examples:

- approve/reject candidate requirements,
- reconsider risks,
- modify Q1/Q2/Q3 behavior,
- change implementation,
- investigate failed tests,
- determine acceptable residual risk,
- determine release readiness.

---

# 17. Conclusions and Recommended Next Actions

Summarize what the system testing activity established.

Provide prioritized next actions.

Do not simply repeat the Executive Summary.

The conclusion should answer:

"What should the engineering team do next based on the testing evidence?"

---

# Appendices

Use appendices for detailed evidence that would make the main report difficult
to read.

Create only appendices supported by available evidence.

Possible appendices include:

## Appendix A — Complete System Test Case Catalog

Detailed test procedures if too large for the main body.

## Appendix B — Complete Requirements Traceability Matrix

Full Requirement → Risk/Q1/Q2/Q3 → Test traceability where available.

## Appendix C — Test Environment and Dependency Inventory

Detailed software, package, framework, database, API, and tool versions.

## Appendix D — Test Execution Evidence

References to logs, screenshots, CI results, test-result files, or other
execution evidence.

## Appendix E — Requirements Discovery Details

Expanded analysis of candidate requirements discovered during testing.

## Appendix F — Repository Evidence References

Relevant files, paths, commits, tags, releases, workflows, and other repository
evidence used to produce the report.

Do not create empty appendices simply to satisfy this structure.

---

# 19. Save the Report

Create or update the System Testing Report in the repository documentation area.

Preferred location:

.github/repo/docs/System-Testing-Report.md

If the repository already uses another clearly established documentation
location, preserve the existing repository convention rather than creating
duplicate structures.

Do not delete previous engineering evidence.

If an earlier System Testing Report exists, update it carefully while preserving
useful historical information.

---

# 20. Final Response to the Student

After creating the report, provide a short summary containing:

- report location,
- strongest testing evidence,
- most important testing gap,
- number of requirements with no identifiable system-test coverage,
- number of Requirements Discovery items,
- highest-priority discovered requirement/risk question,
- recommended next engineering action.

Do not imply that generated tests have been executed.

---

# Engineering Integrity Rules

Throughout this task:

1. Evidence before claims.
2. Never fabricate test execution.
3. Never fabricate PASS results.
4. Never invent repository history.
5. Never convert inferred behavior into verified behavior.
6. Never silently invent missing requirements.
7. Never treat generated tests as executed tests.
8. Never treat unit tests as system tests.
9. Preserve existing requirement identifiers whenever possible.
10. Trace tests to requirements whenever possible.
11. Treat Q1, Q2, and Q3 as distinct verification concerns.
12. Identify missing evidence explicitly.
13. Surface requirements discoveries instead of silently repairing them.
14. Require student judgment for engineering decisions.
15. Treat the repository as the primary source of engineering evidence.

The objective is not to produce a polished report that makes the project look
complete.

The objective is to produce an accurate engineering assessment of what has
actually been implemented, what has actually been verified, what remains
untested, and what new requirements questions have been discovered through
system testing.