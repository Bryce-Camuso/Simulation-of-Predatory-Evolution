# Software Test Plan and Report

**Project:** Predator-Prey Simulation System
**Author:** Bryce Camuso
**Course:** CISC 699
**Semester:** Summer 2026
**Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
**Current branch:** To Be Completed
**Document version:** 0.2
**Document status:** Draft
**Last updated:** 2026-08-05
**Primary test frameworks / artifacts:** None (ad-hoc `tester()` functions inside class modules and simulation drivers)
 
---

# Test execution summary (runs performed 2026-08-05)

I ran the in-repo class-level tester scripts located in the `classes/` folder from the repository root using the workspace Python interpreter. Runs were executed synchronously and outputs were captured from the terminal. Below are the observed outcomes and brief evidence notes copied from the captured console output.

| Artifact run | Outcome | Notes / evidence |
|--------------|---------|------------------|
| `classes/Map.py` | PASS | All Map tester checks printed `pass` (Map Size, Tile Distribution, Getters, Singleton).
| `classes/Scent.py` | PASS | Scent trail get/add/update/decay checks printed `pass` for multiple levels.
| `classes/Plant.py` | PASS | Getters, setters, and `Update Scent Trail` printed `pass`.
| `classes/Animal.py` | PASS | Getters/setters, scent update, search, scent decay, energy use, and pathfinding printed `pass`.
| `classes/Prey.py` | PASS | Getter/setter, move-phase tests, and struggle printed `pass`.
| `classes/Predator.py` | PARTIAL (1 failure) | Most checks passed; `ambush range` test printed `fail` (see console output in appendix).
| `classes/Bird.py` | PASS | Getters/setters and `pathfinding check: pass` observed.
| `classes/Rabbit.py` | PASS | `check_escape: pass` observed.


Execution notes:
- All scripts were executed from the repository root using the configured Python executable for the workspace.
- `classes/Predator.py` produced a failing check for `ambush range` which should be investigated; other Predator tests passed.
- Two modules (`Mouse.py`, `StaticMap.py`) produced no output; they either lack `tester()` functions or their `__main__` sections do not print results.

Recorded terminal outputs are available in the terminal session. Where tests printed `pass` or `fail`, those strings were captured directly from the modules' tester outputs.

---

## Effects on previous status fields

- Execution status for most class-level testers is now `Completed` with captured `pass` outputs as recorded above.
- `classes/Predator.py` is `Partial` due to one failing check (`ambush range: fail`).
- `classes/Mouse.py` and `classes/StaticMap.py` produced no tester output and are marked `To Be Completed` (no evidence of tester execution in those modules).
- `CI/CD status` remains `To Be Completed` (no CI configuration present in the repository).

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