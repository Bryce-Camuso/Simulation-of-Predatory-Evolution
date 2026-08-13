# Software Test Plan and Report

**Project:** Predator-Prey Simulation System
**Author:** Bryce Camuso
**Course:** CISC 699
**Semester:** Summer 2026
**Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
**Current branch:** master
**Current commit SHA:** 92220e7
**Document version:** 0.3
**Document status:** Final
**Last updated:** 2026-08-12
**Primary test frameworks / artifacts:** Ad-hoc `tester()` functions inside class modules; GitHub Actions CI workflow configured to run class tester scripts.
**Configuration management report:** `documents/CONFIGURATION_MANAGEMENT_REPORT.md`

---

# Test artifacts summary

This repository contains developer-written validation artifacts and a CI workflow configuration, but it does not contain a formal Python test suite or committed execution reports.

- `.github/workflows/ci.yml` exists and is configured to run class-level tester modules on `windows-latest` with Python `3.14.4` and `pandas==3.0.3`.
- `classes/Animal.py`, `classes/Bird.py`, `classes/Map.py`, `classes/Mouse.py`, `classes/Plant.py`, `classes/Predator.py`, `classes/Prey.py`, `classes/Rabbit.py`, and `classes/Scent.py` each define `tester()` and an `if __name__ == '__main__'` entry point.
- `classes/Mouse.py` currently defines a no-op `tester()` function (`pass`).
- `classes/StaticMap.py` exists as a dedicated test helper class.
- `requirements.txt` in the repository is a narrative requirements summary, not a standard dependency manifest.
- No dated logs, coverage reports, or other test execution artifacts are committed in the repository.

---

## Repository evidence inventory

- `README.md` — project overview, dependency guidance for Python 3.14.4, and pandas installation instructions.
- `documents/PRD.md` — Product Requirements Document and requirements source.
- `documents/CONFIGURATION_MANAGEMENT_REPORT.md` — configuration management evidence.
- `.github/workflows/ci.yml` — CI workflow configured to validate class tester modules.
- `classes/` modules — production code and inline tester harnesses.
- `simulation-test.py`, `simulation-v1.py`, `simulation-demo.py`, `simulation-v2.py` — simulation drivers and integration-style entry points.
- `csv/` directory — present as output data storage, but no committed test output files were observed.
- `requirements.txt` — narrative project requirements summary, not a pip-style manifest.

---

## Automation and test status

- Test artifact presence: Yes.
- Formal test framework present: No.
- Dependency manifest suitable for automation: No.
- CI configuration present: Yes.
- Committed test execution results: No.

---

## Test execution summary (runs performed 2026-08-12)

The class-level tester modules were executed using package mode from the repository root:

```bash
python -m classes.Animal
python -m classes.Bird
python -m classes.Map
python -m classes.Mouse
python -m classes.Plant
python -m classes.Predator
python -m classes.Prey
python -m classes.Rabbit
python -m classes.Scent
```

The outputs captured from the module executions were:

| Artifact run | Outcome | Notes / evidence |
|--------------|---------|------------------|
| `python -m classes.Animal` | PASS | Animal getters/setters, scent update, search, energy use, and pathfinding checks all printed `pass`.
| `python -m classes.Bird` | PASS | Bird getters/setters and `pathfinding check: pass` were observed.
| `python -m classes.Map` | PASS | Map size, distribution, getters, and singleton checks all printed `pass`.
| `python -m classes.Mouse` | PASS | Module imported successfully, but `tester()` is a no-op and produced no validation output.
| `python -m classes.Plant` | PASS | Plant getters/setters and scent trail update checks all printed `pass`.
| `python -m classes.Predator` | PASS | Predator getters/setters, move-list, ambush, and reproduction checks all printed `pass`.
| `python -m classes.Prey` | PASS | Prey getters/setters, move-list, struggle, and escape logic checks all printed `pass`.
| `python -m classes.Rabbit` | PASS | Rabbit escape check printed `pass`.
| `python -m classes.Scent` | PASS | Scent trail creation, addition, update, and decay checks all printed `pass`.

Execution notes:
- Package execution was required because `classes/` modules use relative imports such as `from .Scent import Scent`.
- `classes/Mouse.py` remains a placeholder tester with no output.
- `classes/StaticMap.py` is used as a support helper but is not itself a standalone test module.
- No committed execution artifacts or reports are present in the repository.

---

## Notes on available validation harnesses

- Each listed class module exposes an ad-hoc `tester()` function that can be run directly.
- The CI workflow is configured to execute the class tester modules by path.
- `classes/Mouse.py` contains a placeholder `tester()` and therefore does not implement a meaningful module-level validation check.
- `classes/StaticMap.py` is a reusable test helper and not itself a formal test case.
- There is no evidence of `pytest` or `unittest` style test files in the repository.

---

## How to run available checks locally

From the repository root, run:

```bash
python classes/Animal.py
python classes/Bird.py
python classes/Map.py
python classes/Mouse.py
python classes/Plant.py
python classes/Predator.py
python classes/Prey.py
python classes/Rabbit.py
python classes/Scent.py
```

Simulation drivers can be executed from the repository root:

```bash
python simulation-test.py
python simulation-v1.py
python simulation-demo.py
python simulation-v2.py
```

Note: Some scripts may require repository-root-relative imports or `sys.path` adjustments. Execute them from the repository root to ensure imports resolve.

---

## Known gaps and recommended next steps

1. Convert inline `tester()` functions into a structured `pytest` or `unittest` suite with assert-based test cases.
2. Replace or supplement the repository narrative `requirements.txt` with a standard dependency manifest such as `requirements.txt` or `pyproject.toml`.
3. Capture and commit CI or local test execution artifacts, and optionally publish logs or coverage reports as workflow artifacts.
4. Implement a meaningful `classes/Mouse.py` tester harness.
5. Add a documented test-results folder and link dated run reports from this document.

---

## Revision history

| Version | Date | Author | Notes |
|--------:|------|--------|-------|
| 0.1 | 2026-07-28 | Repository analysis | Initial living test-plan generated from repository evidence. |
| 0.2 | 2026-08-05 | Draft update | Original draft contained pre-existing assumptions; improved evidence grounding required. |
| 0.3 | 2026-08-12 | GitHub Copilot | Updated to reflect repository evidence: CI workflow exists, inline testers exist, no committed execution artifacts.

---

## Purpose

This document captures the current repository-grounded software test plan and report for the predator-prey simulation project. It avoids assumptions beyond the committed repository contents.

---

## Appendix — files consulted

- `README.md`
- `documents/PRD.md`
- `documents/CONFIGURATION_MANAGEMENT_REPORT.md`
- `.github/workflows/ci.yml`
- `classes/Animal.py`
- `classes/Bird.py`
- `classes/Map.py`
- `classes/Mouse.py`
- `classes/Plant.py`
- `classes/Predator.py`
- `classes/Prey.py`
- `classes/Rabbit.py`
- `classes/Scent.py`
- `simulation-test.py`
- `simulation-v1.py`
- `simulation-demo.py`
- `simulation-v2.py`
- `requirements.txt`

<!-- End of Software Test Plan and Report -->