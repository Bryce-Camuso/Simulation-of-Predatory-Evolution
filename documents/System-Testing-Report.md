# System Testing Report

**Project:** Predator-Prey Simulation System
**Author:** GitHub Copilot
**Date:** 2026-08-12
**Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
**Current branch:** master
**Current commit SHA:** 92220e7
**Document version:** 1.0
**Document status:** Final

---

## Executive Summary

This report documents the current repository evidence for system-level testing in the Predator-Prey Simulation System. The repository contains ad-hoc component validation code, simulation drivers with CSV export, and a GitHub Actions workflow configured to run class-level tester scripts. It does not contain a formal system testing framework, a dedicated `tests/` directory, or committed system test result artifacts.

---

## Repository Evidence

- `README.md` documents Python 3.14.4 and `pandas==3.0.3` as primary runtime dependencies.
- `.github/workflows/ci.yml` exists and is configured to run class-level tester modules on `windows-latest` with Python `3.14.4`.
- `classes/` contains multiple modules with inline `tester()` functions and `if __name__ == '__main__'` entry points.
- `simulation-v2.py`, `simulation-v1.py`, `simulation-demo.py`, and `simulation/simulation-test.py` exist as simulation drivers that accept command-line arguments and export CSV output via pandas.
- `requirements.txt` is present, but its contents are a narrative project requirements summary rather than a standard Python dependency manifest.
- No `documents/System-Testing-Report.md` existed prior to this file.
- No committed test run logs, HTML reports, or coverage artifacts were observed in the repository.

---

## Test Environment Evidence

- Python version targeted: 3.14.4 (README, `.github/workflows/ci.yml`).
- Third-party library targeted: `pandas==3.0.3` (README, `.github/workflows/ci.yml`, simulation drivers).
- Command-line interfaces exist in simulation scripts via `argparse` (seen in `simulation-v2.py`, `simulation-v1.py`, `simulation-demo.py`, `simulation/simulation-test.py`).
- CSV export is implemented in multiple scripts via `pandas.DataFrame.to_csv()` (`simulation-v2.py`, `simulation-v1.py`, `simulation-demo.py`).

---

## System Testing Artifacts and Practices

### Implemented or Present

- Component-level test harnesses exist as inline `tester()` functions in `classes/Animal.py`, `classes/Bird.py`, `classes/Map.py`, `classes/Mouse.py`, `classes/Plant.py`, `classes/Predator.py`, `classes/Prey.py`, `classes/Rabbit.py`, and `classes/Scent.py`.
- A CI workflow file exists at `.github/workflows/ci.yml`.
- Simulation drivers with data export exist in `simulation-v2.py`, `simulation-v1.py`, `simulation-demo.py`, and `simulation/simulation-test.py`.
- A `csv/` directory is present for output data.

### Partially Implemented or Incomplete

- `classes/Mouse.py` defines a `tester()` function, but the function body is a no-op (`pass`).
- `requirements.txt` exists, but it is not a standard dependency manifest and does not provide an executable environment specification.
- The CI workflow is configured to execute `python classes/*.py` directly, while the `classes/` modules use relative imports such as `from .Scent import Scent` and therefore require package-aware execution or `PYTHONPATH` adjustments.

### Not Implemented

- Formal system-level test suites are not present.
- No `tests/` directory or pytest/unittest-style modules are present.
- No documented system test plans, acceptance criteria, or pass/fail result summaries are present in the repository.
- No released or tagged test baselines, release notes, or system test artifact directories were observed.

---

## System Testing Findings

### Testability

- The project structure is class-based and supports direct execution of many modules.
- System testing is not clearly separated from implementation code; validation is embedded in class files rather than in dedicated test modules.
- Simulation scripts are available and appear to exercise the system through command-line execution and CSV export, but they are not explicitly identified as system tests in repository documentation.

### CI/CD and Automation

- CI workflow exists, but the workflow steps may not align with code import semantics in `classes/` modules.
- There is no evidence of successful workflow runs or artifacts committed to the repository.

### Documentation Coverage

- `README.md` documents project dependencies and running scripts.
- `documents/PRD.md` and `documents/Software-Test-Plan-and-Report.md` document requirements and test-plan-related evidence.
- There is no dedicated system testing document before this one.

---

## To Be Completed

- Formal system test cases and test coverage metrics.
- Test execution results and evidence artifact files.
- Test environment reproducibility manifest in standard format (`requirements.txt` or `pyproject.toml`).
- System test plan with acceptance criteria and execution record.
- Automated system test suite or integration tests separate from inline class testers.
- Machine-readable test summary or result reports in `documents/` or `csv/`.

---

## Recommendations

### High Priority

- Add a dedicated system test suite or integration test module set in a `tests/` directory.
- Fix the CI workflow to run tests in a way that matches the repository import structure, such as using `python -m classes.<module>` or adjusting `PYTHONPATH`.
- Create a standard dependency manifest (`requirements.txt` with package pins or `pyproject.toml`) for reproducible test execution.

### Medium Priority

- Implement a meaningful `classes/Mouse.py` tester function or move its validation into a dedicated test module.
- Add a `documents/System-Testing-Report.md` section linking to actual test artifact locations and execution commands.
- Capture and commit test run outputs, logs, or coverage reports as repository evidence.

### Future Improvements

- Define system test acceptance criteria and include them in repository documentation.
- Add system-level regression tests for key simulation behavior and CSV output validation.
- Add a test-results directory for dated system test run artifacts.

---

## Revision History

| Version | Date | Notes |
|--------|------|-------|
| 1.0 | 2026-08-12 | Initial system testing report created from repository evidence. |
