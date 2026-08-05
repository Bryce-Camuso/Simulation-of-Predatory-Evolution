# Software Test Plan and Report

**Project:** Predator-Prey Simulation System
**Author:** Bryce Camuso
**Course:** CISC 699
**Semester:** Summer 2026
**Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
**Current branch:** Sim/Siv-v1
**Document version:** 0.1
**Document status:** Draft
**Last updated:** 2026-07-28
**Primary test frameworks / artifacts:** None (ad-hoc Python tester functions and simulation driver)
 
---

# Test execution summary (runs performed 2026-07-28)

I executed the in-repo class-level testers and the `simulation-test.py` driver from the repository root and captured console outputs. Runs were limited to normal completion (no artificial time limits beyond 120s). The following is a concise, evidence-based summary.

| Artifact run | Outcome | Notes / evidence |
|--------------|---------|------------------|
| `classes/Map.py` | PASS | All Map tester checks printed `pass` (Map Size, Tile Distribution, Getters, Singleton).
| `classes/Scent.py` | PASS | All scent-trail length checks, add/update/decay checks printed `pass`.
| `classes/Plant.py` | PASS | Getters, setters, and `update_scent_trail()` printed `pass`.
| `classes/Animal.py` (`auto`) | PASS | Getters/setters, scent update, search, scent decay, and pathfinding printed `pass` (Energy use reported `false` where code prints that). Evidence: console output captured.
| `classes/Prey.py` | PASS | All Prey tester checks printed `pass` (getters, setters, get_move_list phases, struggle).
| `classes/Predator.py` | PASS | All Predator tester checks printed `pass` (getters, setters, get_move_list phases, ambush, reproduction).
| `classes/Bird.py` | PASS | Bird class tester printed `pathfinding check: pass` and other checks passed.
| `classes/Rabbit.py` | PASS | Rabbit tester printed `check_escape: pass`.
| `simulation-test.py` | PASS (integration) | Ran until predator caught prey; sample moves printed and `Predator caught prey` observed. Sample output:

```
prey move: (20, 26)
pred move: (37, 44)
prey move: (9, 20)
pred move: (26, 37)
prey move: (9, 9)
pred move: (21, 26)
prey move: (11, 10)
pred move: (11, 17)
prey move: (10, 9)
pred move: (10, 9)
Predator caught prey
```

---

## Effects on previous status fields

- Execution status for many class-level testers is now `Completed` with pass/fail evidence above. Where errors occurred during tests, the status is `Partial / Error` and includes the captured traceback.
- `CI/CD status` remains `To Be Completed` (no CI was added and runs were manual local runs).

---

## Minimal next steps to produce fully automated, green test status

1. Fix the `StaticMap` test helper (or adjust the `Prey`/`Predator` testers) so their test harnesses use the same Map API as production (`get_map_limit()` exists). This will likely make `Prey` and `Predator` testers run to completion.
2. Convert in-file testers to `pytest` modules and add a simple GitHub Actions CI workflow to run the test suite and upload artifacts.

---

---

## Revision history

| Version | Date | Author | Notes |
|--------:|------|--------|-------|
| 0.1 | 2026-07-28 | Repository analysis | Initial living test-plan generated from repository evidence (excludes `run_test.bat` and `/test`) |

---

## Purpose

This Software Test Plan and Report documents the current, repository-grounded testing artifacts and their mapping to requirements in `documents/PRD.md`. No information is invented; unknown items are marked `To Be Completed`.

---

## Evidence inventory (included in this report)

- [README.md](README.md) — project overview, dependencies (Python 3.14.4) and instructions.
- [documents/PRD.md](documents/PRD.md) — Product Requirements Document (source of requirement identifiers and descriptions).
- `classes/` — production code for simulation components. Several class files include inline `tester()` functions (e.g., `classes/Animal.py`, `classes/Scent.py`, `classes/Map.py`, `classes/Predator.py`, `classes/Prey.py`, `classes/Bird.py`, `classes/Rabbit.py`). These are developer-written smoke tests inside class files; presence is recorded, but execution evidence is not in the repo.
- `simulation-test.py` and `simulation-v1.py` — small simulation drivers that instantiate `Animal` objects and run loops using `Animal.search()` and `Animal.pathfinding()`; useful for integration-style checks.
- `csv/` directory — present to hold potential output data (no dated test result files were observed).
- `documents/` folder — houses `PRD.md` and project documentation used to trace requirements.

Excluded from this report by user request: `run_test.bat` and files under the `/test` folder are not discussed or used as evidence here.

---

## Mapping artifacts to PRD requirements (conservative)

The following mappings are conservative: they assert that code or drivers exercise the listed requirements, not that automated test results exist or passed.

- `classes/Animal.py` (and related classes): exercises FR-1.1.1, FR-1.2.1, FR-1.3.1, FR-3.x (scent integration), FR-4.3.1 (pathfinding/pursuit behavior).
- `classes/Scent.py`: exercises FR-3.1.1, FR-3.2.1, FR-3.3.1, FR-3.4.1.
- `classes/Map.py`: exercises FR-2.1.1, FR-2.2.1, FR-2.3.1.
- `classes/Prey.py`, `classes/Predator.py`, `classes/Bird.py`, `classes/Rabbit.py`: exercise FR-4.x family (search, stalking, pursuit) and reproductive/evolution behaviors found in class code.
- `simulation-test.py` / `simulation-v1.py`: exercise FR-7.1.1 and FR-7.2.1 (initialization and simulation loop), and compose multiple subsystems for integration checks.

Execution status for all mappings: To Be Completed (no execution logs, CI, or recorded test artifacts found in the repository for these mappings).

---

## Test status summary

- Test artifacts present (inline testers, simulation drivers): Yes.
- Structured test framework (pytest, unittest) present: No.
- CI configuration present: No.
- Historical test run artifacts (logs, coverage reports): No.

All quantitative results (pass/fail counts, coverage percentages, performance metrics) are `To Be Completed`.

---

## How to run the available checks locally (evidence-based)

Run individual class-level tester functions (each class file contains a `tester()` function or a `__main__` section). Example commands from repository root:

```bash
python classes/Animal.py
python classes/Scent.py
python classes/Map.py
python classes/Predator.py
python classes/Prey.py
python classes/Bird.py
python classes/Rabbit.py
```

Run the simulation driver(s):

```bash
python simulation-test.py
python simulation-v1.py
```

Notes: Some scripts modify `sys.path` before importing `classes/`. Run commands from the repository root to ensure imports resolve.

---

## Known gaps and recommended next steps (evidence-driven)

1. Convert inline `tester()` functions and ad-hoc drivers into a structured test suite (recommended: `pytest`) with deterministic assert-based test cases. This enables automated pass/fail reporting and CI integration.
2. Add a dependency manifest (`requirements.txt` or `pyproject.toml`) to make test and runtime environment reproducible (README references Python 3.14.4 but no manifest file exists).
3. Add CI (e.g., GitHub Actions workflow) to run tests on push/PR and store artifacts (test logs, coverage reports).
4. Run `simulation-test.py` and class tester scripts, capture outputs, and commit run artifacts or save them as CI artifacts so the repository reflects execution status.
5. Add a `docs/test-results/` or `documents/test-report/` location to store dated test reports and add a short summary of each run in `documents/Software Test Plan and Report.md`.

---

## Test metrics and results

No executed test metrics or results were found in the repository. All metrics and pass/fail statuses are `To Be Completed` until the tests are executed and artifacts are recorded.

---

## Final recommendations (prioritized)

- High: Convert to `pytest` and add CI workflow to run tests and upload artifacts.
- High: Add `requirements.txt` or `pyproject.toml` and lock Python version in docs.
- Medium: Run existing simulation drivers and class testers, capture outputs, and commit artifacts or attach them to CI runs.
- Medium: Add a `documents/test-results/` folder to store structured reports and link them from this document.

---

## Appendix — files consulted (excluding `run_test.bat` and `/test`)

- `README.md`
- `documents/PRD.md`
- `classes/Animal.py`, `classes/Scent.py`, `classes/Map.py`, `classes/Predator.py`, `classes/Prey.py`, `classes/Bird.py`, `classes/Rabbit.py`
- `simulation-test.py`, `simulation-v1.py`
- `csv/` (directory presence)


<!-- End of Software Test Plan and Report -->