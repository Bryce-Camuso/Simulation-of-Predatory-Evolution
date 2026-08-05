# Product Requirements Document

**Predator-Prey Simulation System**

---

# Cover Page

- **Project Name:** Predator-Prey Simulation System
- **Student(s):** Bryce Camuso
- **Course:** CISC 699
- **Semester:** Summer 2026
- **Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
- **Current Branch:** Master
- **Current Commit SHA:** 6b846f4
- **Current Release Version:** 0.1
- **Document Version:** 0.4
- **Last Updated:** 2026-08-05

---

# Revision History

| Version | Date | Git Commit | Description | Author |
|----------|------|------------|-------------|--------|
| 0.1 | 2026-07-21 | test PRD | Initial PRD scaffold created from prompt structure. | Bryce Camuso |
| 0.2 | 2026-07-21 | PRD update with prompts | Updated PRD based on repository evidence: predator-prey simulation with scent tracking, map-based navigation, and multiple animal types. | Bryce Camuso |
| 0.3 | 2026-07-25 | PRD manual update | Updated PRD to better reflect the projects intentions that have not been reflected in code yet. | Bryce Camuso |
| 0.4 | 2026-08-05 | 6b846f4 | Updated PRD to align scope, features, and testing with the current repository implementation. | Bryce Camuso |

---

# Table of Contents

- [Cover Page](#cover-page)
- [Revision History](#revision-history)
- [Table of Contents](#table-of-contents)
- [1. Product Vision](#1-product-vision)
- [2. Product Scope](#2-product-scope)
- [3. Software Capabilities](#3-software-capabilities)
  - [3.1 Level-1 Capabilities](#31-level-1-capabilities)
  - [3.2 Level-2 Capabilities](#32-level-2-capabilities)
- [4. Undesirable Events](#4-undesirable-events)
- [5. Risk Analysis](#5-risk-analysis)
- [6. Risk Prioritization](#6-risk-prioritization)
- [7. Risk Mitigation](#7-risk-mitigation)
- [8. Functional Requirements](#8-functional-requirements)
- [9. Quality Requirements](#9-quality-requirements)
- [10. Performance Requirements](#10-performance-requirements)
- [11. Assumptions](#11-assumptions)
- [12. Constraints](#12-constraints)
- [13. External Interfaces](#13-external-interfaces)
- [14. Requirements Traceability Matrix](#14-requirements-traceability-matrix)
- [15. Future Versions](#15-future-versions)
- [16. Open Issues](#16-open-issues)
- [17. Glossary](#17-glossary)

---

# 1. Product Vision

## Problem Statement

Provide a Python-based predator-prey simulation prototype that models animal movement, sensing, hunting, and energy management in a bounded 2D grid environment. The system should demonstrate map-based navigation, scent trail propagation, and strategy-driven predator/prey interactions.

## Intended Users

- Students studying simulation systems and agent-based behaviors
- Educators demonstrating prototype ecosystem models
- Developers exploring Python simulation design

## Stakeholders

- CISC 699 Course Instructor
- Student Developer
- Repository Maintainers

## Product Goals

- Implement a working predator-prey simulation prototype in Python
- Support configurable animal attributes and class-based behaviors
- Provide ambush and pursuit predator hunting strategies
- Implement scent trail generation and decay for navigation
- Enable command-line simulation execution with CSV export
- Maintain inline component validation via tester functions

## Major Features

- **Animal Class Hierarchy:** `Animal` base class with subclasses `Predator`, `Prey`, `Bird`, `Rabbit`, and `Mouse`
- **Map-Based Environment:** `Map` class with random tile generation and `StaticMap` test helper
- **Scent Trail System:** `Scent` class for scent generation, lookup, and decay
- **Movement and Pathfinding:** Weight-based pathfinding and movement across grid tiles
- **Predator Hunting Strategies:** Ambush and pursuit modes with range and stalking logic
- **Prey Behavior:** Escape behavior and type-specific checks for rabbit and bird
- **CSV Output:** Export simulation results using `pandas`
- **Tester Functions:** Inline `tester()` methods in modules for component verification

## Planned Software Versions

- **Version 0.1:** Current prototype with animal classes, map, scent system, and simulation drivers
- **Version 1.0:** Expanded validation and more complete behavior coverage
- **Version 2.0:** Additional species, richer behaviors, and enhanced analysis support

---

# 2. Product Scope

## Included Functionality

- Animal class hierarchy with attribute management in `classes/Animal.py`, `classes/Predator.py`, and `classes/Prey.py`
- Specialized prey classes `Bird`, `Rabbit`, and `Mouse` with type-specific behavior hooks
- `Map` generation and tile access methods in `classes/Map.py`
- `StaticMap` test helper for deterministic map access in validation code
- Scent trail generation, lookup, and decay logic in `classes/Scent.py`
- Pathfinding and weight-based movement decision functions for animals
- Predator hunting strategy logic for ambush and pursuit
- Rabbit escape check based on bush tiles and bird in-air state tracking
- Command-line simulation drivers (`simulation-test.py`, `simulation-v1.py`) with CSV export
- Inline module tester functions for manual component verification

## Excluded Functionality

- GUI or graphical visualization layer
- Formal automated unit test framework or test runner
- Networked or distributed simulation execution
- Persistent database storage beyond CSV files
- Realtime interactive simulation control beyond command-line arguments

## Future Enhancements

- Formal automated test harness and coverage reporting
- Additional predator and prey species with richer behaviors
- Improved simulation configuration and runtime parameter tuning
- Environment hazards, obstacles, and weather impact modeling
- Performance optimization for larger population sizes

---

# 3. Software Capabilities

The capabilities below reflect the current prototype implementation and its planned expansion path for animal movement, map navigation, scent tracking, and a simple predator-prey simulation loop.

## 3.1 Level-1 Capabilities

1. **Manage Prototype Animal State and Behavior**
2. **Navigate and Track Position on Map**
3. **Generate and Track Scent Trails**
4. **Execute Search and Pursuit Strategies**
5. **Monitor Energy and Stamina**
6. **Output and Analyze Simulation Results**
7. **Execute and Validate Simulation**

## 3.2 Level-2 Capabilities

1. Manage Animal State and Behavior

1.1 Initialize Animal with Attributes  
1.2 Update Animal Attributes  
1.3 Execute Animal Movement  
1.4 Determine Animal Search Behavior  

2. Navigate and Track Position on Map

2.1 Define Map Structure and Tile Types  
2.2 Track Animal Position  
2.3 Calculate Movement Constraints  
2.4 Build Prey Item Class  

3. Generate and Track Scent Trails

3.1 Create and Initialize Scent Trail  
3.2 Update Scent Trail Over Time  
3.3 Decay Scent at Specified Rate  
3.4 Retrieve Scent Values  

4. Execute Search and Pursuit Strategies

4.1 Execute Search Behavior  
4.2 Execute Stalking Behavior  
4.3 Execute Pursuit Behavior  
4.4 Determine Predator Catch Success  

5. Monitor Energy and Stamina

5.1 Calculate Stamina Consumption  
5.2 Track Energy Level Changes  
5.3 Detect Energy Depletion  
5.4 Update Remaining Stamina  

6. Output and Analyze Simulation Results

6.1 Export Simulation Data to CSV  
6.2 Format Output Data Correctly  
6.3 Write Data Records  

7. Execute and Validate Simulation

7.1 Initialize Simulation Environment  
7.2 Run Simulation Loop  
7.3 Validate Test Results  
7.4 Execute Batch Test Suite  

---

# 4. Undesirable Events

| UE ID | Level-2 Capability | Undesirable Event |
|-------|--------------------|-------------------|
| UE-1.1-01 | Initialize Animal with Attributes | Animal created with invalid or missing attributes |
| UE-1.2-01 | Update Animal Attributes | Attribute update causes inconsistent animal state |
| UE-1.3-01 | Execute Animal Movement | Animal moves outside map boundaries |
| UE-1.4-01 | Determine Animal Search Behavior | Incorrect search strategy selected for animal type |
| UE-2.1-01 | Define Map Structure and Tile Types | Map contains invalid or unbalanced tile distribution |
| UE-2.2-01 | Track Animal Position | Position tracking diverges from actual animal location |
| UE-2.3-01 | Calculate Movement Constraints | Movement constraints not applied correctly |
| UE-2.4-01 | Build Prey Item Class | Prey item not properly integrated with map |
| UE-3.1-01 | Create and Initialize Scent Trail | Scent trail initialized with incorrect parameters |
| UE-3.2-01 | Update Scent Trail Over Time | Scent trail updates are inconsistent or delayed |
| UE-3.3-01 | Decay Scent at Specified Rate | Scent decay does not follow specified decay model |
| UE-3.4-01 | Retrieve Scent Values | Incorrect scent values returned for location |
| UE-4.1-01 | Execute Search Behavior | Predator does not locate prey using search strategy |
| UE-4.2-01 | Execute Stalking Behavior | Stalking behavior fails to track prey movement |
| UE-4.3-01 | Execute Pursuit Behavior | Pursuit fails to catch prey despite proximity |
| UE-4.4-01 | Determine Predator Catch Success | Catch determination uses incorrect criteria |
| UE-5.1-01 | Calculate Stamina Consumption | Stamina consumption does not match movement distance |
| UE-5.2-01 | Track Energy Level Changes | Energy changes not properly tracked |
| UE-5.3-01 | Detect Energy Depletion | Energy depletion not detected when stamina expires |
| UE-5.4-01 | Update Remaining Stamina | Stamina update fails or produces negative values |
| UE-6.1-01 | Export Simulation Data to CSV | CSV file not created or is corrupted |
| UE-6.2-01 | Format Output Data Correctly | Data formatted incorrectly in output |
| UE-6.3-01 | Write Data Records | Data records not written to output file |
| UE-7.1-01 | Initialize Simulation Environment | Simulation environment not properly initialized |
| UE-7.2-01 | Run Simulation Loop | Simulation loop terminates prematurely |
| UE-7.3-01 | Validate Test Results | Test validation produces false positives or negatives |
| UE-7.4-01 | Execute Batch Test Suite | Batch test suite fails to execute all tests |

---

# 5. Risk Analysis

| UE ID | Risk Statement | Likelihood | Impact | Risk Score |
|-------|----------------|------------|--------|------------|
| UE-1.1-01 | Invalid animal initialization could cause runtime errors. | 3 | 4 | 12 |
| UE-1.2-01 | Inconsistent attribute updates could corrupt animal state. | 2 | 4 | 8 |
| UE-1.3-01 | Out-of-bounds movement could cause simulation crashes. | 3 | 4 | 12 |
| UE-1.4-01 | Incorrect search behavior selection could break predator logic. | 2 | 4 | 8 |
| UE-2.1-01 | Invalid map structure could skew simulation results. | 2 | 3 | 6 |
| UE-2.2-01 | Position tracking errors could accumulate over simulation. | 3 | 3 | 9 |
| UE-2.3-01 | Unenforced movement constraints could produce invalid movement. | 3 | 3 | 9 |
| UE-2.4-01 | Improper prey integration could break scent tracking. | 2 | 4 | 8 |
| UE-3.1-01 | Invalid scent initialization could break decay mechanics. | 2 | 3 | 6 |
| UE-3.2-01 | Inconsistent scent updates could produce unrealistic trails. | 3 | 3 | 9 |
| UE-3.3-01 | Incorrect decay rate could make scent tracking unusable. | 3 | 4 | 12 |
| UE-3.4-01 | Incorrect scent values could prevent predator tracking. | 3 | 4 | 12 |
| UE-4.1-01 | Failed search behavior could make predators unable to hunt. | 4 | 4 | 16 |
| UE-4.2-01 | Failed stalking could break predator-prey dynamics. | 4 | 4 | 16 |
| UE-4.3-01 | Failed pursuit could break the complete hunt sequence. | 4 | 4 | 16 |
| UE-4.4-01 | Incorrect catch criteria could make predators always miss. | 3 | 4 | 12 |
| UE-5.1-01 | Incorrect stamina consumption could make animals unrealistic. | 2 | 3 | 6 |
| UE-5.2-01 | Incorrect energy tracking could break game mechanics. | 3 | 3 | 9 |
| UE-5.3-01 | Failure to detect depletion could allow invalid animal states. | 2 | 3 | 6 |
| UE-5.4-01 | Stamina update errors could cause state corruption. | 2 | 3 | 6 |
| UE-6.1-01 | Missing CSV output could prevent result analysis. | 2 | 3 | 6 |
| UE-6.2-01 | Malformed CSV data could break downstream analysis. | 2 | 2 | 4 |
| UE-6.3-01 | Failure to write records could lose simulation results. | 2 | 3 | 6 |
| UE-7.1-01 | Poor initialization could invalidate entire simulation. | 2 | 4 | 8 |
| UE-7.2-01 | Premature termination could prevent results collection. | 2 | 3 | 6 |
| UE-7.3-01 | Invalid test validation could hide defects. | 3 | 4 | 12 |
| UE-7.4-01 | Failed batch tests could prevent regression detection. | 2 | 3 | 6 |

---

# 6. Risk Prioritization

| Priority | UE ID | Risk Score |
|----------|-------|------------|
| 1 | UE-4.1-01 | 16 |
| 2 | UE-4.2-01 | 16 |
| 3 | UE-4.3-01 | 16 |
| 4 | UE-1.1-01 | 12 |
| 5 | UE-1.3-01 | 12 |
| 6 | UE-3.3-01 | 12 |
| 7 | UE-3.4-01 | 12 |
| 8 | UE-4.4-01 | 12 |
| 9 | UE-7.3-01 | 12 |
| 10 | UE-1.2-01 | 8 |
| 11 | UE-1.4-01 | 8 |
| 12 | UE-2.4-01 | 8 |
| 13 | UE-7.1-01 | 8 |
| 14 | UE-2.2-01 | 9 |
| 15 | UE-2.3-01 | 9 |
| 16 | UE-3.2-01 | 9 |
| 17 | UE-5.2-01 | 9 |
| 18 | UE-2.1-01 | 6 |
| 19 | UE-3.1-01 | 6 |
| 20 | UE-5.1-01 | 6 |
| 21 | UE-5.3-01 | 6 |
| 22 | UE-5.4-01 | 6 |
| 23 | UE-6.1-01 | 6 |
| 24 | UE-6.3-01 | 6 |
| 25 | UE-7.2-01 | 6 |
| 26 | UE-7.4-01 | 6 |
| 27 | UE-6.2-01 | 4 |

---

# 7. Risk Mitigation

| UE ID | Risk Mitigation | Classification |
|-------|-----------------|----------------|
| UE-1.1-01 | Implement constructor validation and unit tests for all animal types. | Pure Software |
| UE-1.2-01 | Use property setters with validation; maintain invariant checks. | Pure Software |
| UE-1.3-01 | Enforce boundary checking before and after movement calculations. | Pure Software |
| UE-1.4-01 | Document search strategy selection logic; add unit tests for each type. | Pure Software |
| UE-2.1-01 | Validate map structure during initialization and log tile distribution. | Pure Software |
| UE-2.2-01 | Implement position getter/setter with assertions; log position changes. | Pure Software |
| UE-2.3-01 | Document movement constraints; validate before movement execution. | Pure Software |
| UE-2.4-01 | Test prey integration with scent system; verify correct initialization. | Pure Software |
| UE-3.1-01 | Implement scent constructor with parameter validation and defaults. | Pure Software |
| UE-3.2-01 | Document scent update algorithm; verify decay mechanics in unit tests. | Pure Software |
| UE-3.3-01 | Use configurable decay rate; validate through unit tests and simulation. | Pure Software |
| UE-3.4-01 | Implement getter with boundary checks; test across all map locations. | Pure Software |
| UE-4.1-01 | Implement search algorithm with unit tests; verify behavior in simulation. | Pure Software |
| UE-4.2-01 | Implement stalking algorithm; test predator-prey interaction. | Pure Software |
| UE-4.3-01 | Implement pursuit algorithm; test catch distance calculation. | Pure Software |
| UE-4.4-01 | Document catch criteria; verify through simulation testing. | Pure Software |
| UE-5.1-01 | Document stamina formula; verify calculations in unit tests. | Pure Software |
| UE-5.2-01 | Implement energy tracking with getters/setters; log changes during simulation. | Pure Software |
| UE-5.3-01 | Implement depletion check; trigger state change when stamina < threshold. | Pure Software |
| UE-5.4-01 | Use saturating arithmetic; prevent negative stamina values. | Pure Software |
| UE-6.1-01 | Implement CSV writer with error handling; verify file creation. | Pure Software |
| UE-6.2-01 | Validate CSV format against test cases; verify field delimiters. | Pure Software |
| UE-6.3-01 | Implement write operations with error checking; log write failures. | Pure Software |
| UE-7.1-01 | Implement initialization checklist; verify all components ready before simulation. | Pure Software |
| UE-7.2-01 | Implement simulation loop with termination conditions; set maximum iterations. | Pure Software |
| UE-7.3-01 | Define validation criteria explicitly; review test cases before execution. | Pure Software |
| UE-7.4-01 | Implement batch runner to execute all tests; report pass/fail for each. | Pure Software |

---

# 8. Functional Requirements

| Requirement ID | Level-2 Capability | Functional Requirement |
|----------------|--------------------|------------------------|
| FR-1.1.1 | Initialize Animal with Attributes | The Animal Factory shall initialize each prototype animal with required attributes (speed, stealth, stamina, sense, position, energy) within the constructor. |
| FR-1.2.1 | Update Animal Attributes | The Animal State Manager shall provide getter/setter methods for all animal attributes with validation. |
| FR-1.3.1 | Execute Animal Movement | The Movement Engine shall calculate new animal position based on current position, speed, and direction within map boundaries. |
| FR-1.4.1 | Determine Animal Search Behavior | The Behavior Selector shall select the appropriate search strategy (Search, Stalking, Pursuit) for the active predator-prey prototype based on behavior context. |
| FR-2.1.1 | Define Map Structure and Tile Types | The Map Builder shall create a 2D grid with configurable tile types (Plain, Tree, Bush) and validate tile distribution. |
| FR-2.2.1 | Track Animal Position | The Position Tracker shall maintain current (x, y) coordinates for each animal and update after movement. |
| FR-2.3.1 | Calculate Movement Constraints | The Constraint Engine shall enforce boundary checks and prevent animals from moving outside the map. |
| FR-2.4.1 | Build Prey Item Class | The Prey Factory shall instantiate prey-oriented prototype entities and integrate them with the map for simulation use. |
| FR-3.1.1 | Create and Initialize Scent Trail | The Scent Factory shall initialize Scent objects with decay rate and initial intensity at animal position. |
| FR-3.2.1 | Update Scent Trail Over Time | The Scent Manager shall update scent distribution across the map for each simulation tick. |
| FR-3.3.1 | Decay Scent at Specified Rate | The Decay Engine shall reduce scent intensity by specified percentage per level distance. |
| FR-3.4.1 | Retrieve Scent Values | The Scent Query Service shall return current scent value at any map location within one operation. |
| FR-4.1.1 | Execute Search Behavior | The Search Engine shall implement prey detection using scent trail following and return prey location when found. |
| FR-4.2.1 | Execute Stalking Behavior | The Stalk Engine shall track prey movement within sense range and update pursuit path each tick. |
| FR-4.3.1 | Execute Pursuit Behavior | The Pursuit Engine shall calculate shortest path to prey and close distance each tick until catch. |
| FR-4.4.1 | Determine Predator Catch Success | The Catch Detector shall determine when predator and prey occupy same location and mark prey as caught. |
| FR-5.1.1 | Calculate Stamina Consumption | The Stamina Calculator shall decrement stamina based on distance moved and terrain type. |
| FR-5.2.1 | Track Energy Level Changes | The Energy Tracker shall update energy after each animal action (movement, eating, etc.). |
| FR-5.3-01 | Detect Energy Depletion | The Depletion Detector shall identify when stamina reaches zero and trigger animal inactivity. |
| FR-5.4.1 | Update Remaining Stamina | The Stamina Manager shall maintain stamina as positive value and update after each movement. |
| FR-6.1.1 | Export Simulation Data to CSV | The CSV Exporter shall write simulation results to file in CSV format with proper headers. |
| FR-6.2.1 | Format Output Data Correctly | The Data Formatter shall ensure all data fields are correctly delimited and formatted. |
| FR-6.3.1 | Write Data Records | The Record Writer shall append each simulation result as a new row in the CSV file. |
| FR-7.1.1 | Initialize Simulation Environment | The Simulation Initializer shall create the map, prototype animals, and scent system and verify all core components are ready. |
| FR-7.2.1 | Run Simulation Loop | The Simulation Engine shall execute the main loop for each time step and update the prototype predator, prey, and plant entities. |
| FR-7.3.1 | Validate Test Results | The Test Validator shall compare expected and actual test outcomes and report pass/fail. |
| FR-7.4.1 | Execute Batch Test Suite | The Batch Runner shall execute all test files and collect results for reporting. |

---

# 9. Quality Requirements

| Category | Requirement |
|----------|-------------|
| **Performance** | The prototype shall complete small simulation runs without unreasonable delay on standard hardware. |
| **Reliability** | Animals shall maintain valid state (within map bounds, non-negative energy) throughout execution. |
| **Availability** | The code shall run without unexpected crashes for supported command-line scenarios. |
| **Maintainability** | Classes shall be organized by responsibility and support direct inspection through tester functions. |
| **Scalability** | The implementation shall support the current prototype workload; larger population scaling is future work. |
| **Usability** | Command-line behavior and tester output shall be clear and readable. |
| **Security** | File I/O operations shall avoid unhandled exceptions and report permission errors. |
| **Portability** | The prototype shall run on Python 3.14.4 and use standard Python libraries where possible. |
| **Interoperability** | CSV output shall remain readable by standard spreadsheet tools. |
| **Testability** | Public class methods shall be callable from the inline tester functions; formal coverage metrics are To Be Completed. |

---

# 10. Performance Requirements

| Requirement | Status |
|-------------|--------|
| Simulation runtime for small test scenario | To Be Completed |
| CSV export performance for production data | To Be Completed |
| Memory usage per animal | To Be Completed |
| Maximum concurrent animals | To Be Completed |
| Scent trail decay computation | To Be Completed |
| Position calculation latency | To Be Completed |

---

# 11. Assumptions

- Python 3.14.4 is available on the development and test machines.
- The map is a finite 2D bounded grid with fixed dimensions in the current prototype.
- Animals move in discrete steps driven by pathfinding and decision logic.
- Scent is represented as a decaying trail over discrete grid locations.
- Energy and stamina are the primary state variables affecting animal movement.
- Simulation termination is driven by prey escape, prey capture, or exhaustion conditions in the current code.
- Current validation is based on inline module tester functions rather than a formal test harness.

---

# 12. Constraints

| Constraint | Value |
|------------|-------|
| **Programming Language** | Python 3.14.4 |
| **Operating System** | Windows, macOS, Linux |
| **Required Libraries** | random, math, heapq, argparse, concurrent.futures, pandas |
| **Framework** | None (pure Python) |
| **Database** | CSV file format (no database engine) |
| **Hardware** | Standard developer workstation with 4+ GB RAM |
| **External APIs** | None required |
| **Map Grid Size** | 301 × 301 points (0 through 300) for `Map` |
| **Maximum Simulation Ticks** | To Be Completed |

---

# 13. External Interfaces

## User Interfaces

- Command-line interface for running simulations
- Batch test scripts (.bat files on Windows)
- Python module imports for programmatic use

## Hardware Interfaces

- None (standard I/O devices only)

## Software Interfaces

- Python standard library: random, math, heapq, argparse, concurrent.futures
- Third-party library: pandas
- CSV file system interface
- File I/O for data export

## Communication Interfaces

- None (local execution only)

## External Services

- None required

---

# 14. Requirements Traceability Matrix

| Requirement ID | Level-2 Capability | Requirement Description |
|----------------|--------------------|------------------------|
| FR-1.1.1 | Initialize Animal with Attributes | Initialize each prototype animal with required attributes in the constructor |
| FR-1.2.1 | Update Animal Attributes | Provide getter/setter methods with validation |
| FR-1.3.1 | Execute Animal Movement | Calculate a new position based on speed, direction, and map constraints |
| FR-1.4.1 | Determine Animal Search Behavior | Select the appropriate search strategy for the active predator-prey prototype |
| FR-2.1.1 | Define Map Structure and Tile Types | Create a 2D grid with configurable tile types |
| FR-2.2.1 | Track Animal Position | Maintain and update (x, y) coordinates |
| FR-2.3.1 | Calculate Movement Constraints | Enforce map boundary checks |
| FR-2.4.1 | Build Prey Item Class | Instantiate prey-oriented prototype entities for simulation use |
| FR-3.1.1 | Create and Initialize Scent Trail | Initialize Scent with decay rate and intensity |
| FR-3.2.1 | Update Scent Trail Over Time | Update scent distribution each tick |
| FR-3.3.1 | Decay Scent at Specified Rate | Reduce intensity by percentage per distance |
| FR-3.4.1 | Retrieve Scent Values | Return scent value at any location |
| FR-4.1.1 | Execute Search Behavior | Implement scent trail following |
| FR-4.2.1 | Execute Stalking Behavior | Track prey movement within sense range |
| FR-4.3.1 | Execute Pursuit Behavior | Calculate path to prey and close distance |
| FR-4.4.1 | Determine Predator Catch Success | Detect when predator and prey occupy same location |
| FR-5.1.1 | Calculate Stamina Consumption | Decrement stamina based on movement |
| FR-5.2.1 | Track Energy Level Changes | Update energy after each action |
| FR-5.3.1 | Detect Energy Depletion | Identify when stamina reaches zero |
| FR-5.4.1 | Update Remaining Stamina | Maintain positive stamina value |
| FR-6.1.1 | Export Simulation Data to CSV | Write results to CSV file |
| FR-6.2.1 | Format Output Data Correctly | Ensure proper field delimiters |
| FR-6.3.1 | Write Data Records | Append results as new rows |
| FR-7.1.1 | Initialize Simulation Environment | Create and verify all components |
| FR-7.2.1 | Run Simulation Loop | Execute main loop for each tick |
| FR-7.3.1 | Validate Test Results | Compare expected vs. actual outcomes |
| FR-7.4.1 | Execute Batch Test Suite | Execute all tests and report results |

---

# 15. Future Versions

## Version 0.2 (Current Prototype)

- Working predator-prey-plant prototype with map-based movement and scent tracking
- Functional animal, map, and scent classes with testable behavior
- Basic search and pursuit logic implemented through the current simulation harness
- Unit tests covering core components and simulation behaviors
- CSV-compatible simulation artifacts for analysis and reporting

## Version 1.0

- Expanded base simulation with more complete predator and prey behavior trees
- Additional animal subclasses and richer interaction rules
- Improved test coverage and validation for larger simulation runs
- More robust CSV output and result analysis support

## Version 2.0

- Real-time parameter adjustment during simulation
- Advanced scent diffusion algorithms and richer environment rules
- Additional animal species and behavioral variants
- Performance profiling and optimization for larger simulations

## Future Enhancements

- Genetic algorithm for trait evolution
- Multi-predator/multi-prey dynamics
- Seasonal behavior changes
- Hibernation and reproduction mechanics
- Integration with ecology research datasets

---

# 16. Open Issues

- Animals are getting stuck and causing a crash.
- What are the maximum simulation time steps?
- How should ties or draws be handled in tests?
- What format should the CSV headers follow?
- Are there any performance targets for large simulations (100+ animals)?

---

# 17. Glossary

| Term | Definition |
|------|-----------|
| **Animal** | Base class representing any entity in the simulation (predator, prey, plant). |
| **Predator** | Animal class specialized for hunting prey; includes search, stalking, pursuit behaviors. |
| **Prey** | Animal class specialized for evading predators; includes movement and energy management. |
| **Scent** | Environmental marker left by animals; decays over time and distance. |
| **Map** | 2D grid environment containing animals and terrain tiles. |
| **Tile** | Individual cell in the map grid; types include Plain, Tree, Bush. |
| **Stamina** | Energy resource consumed by animal movement; regenerates or depletes based on activity. |
| **Sense** | Animal ability to detect scent trails and prey within range. |
| **Search** | Predator behavior of following scent trails to locate prey. |
| **Stalking** | Predator behavior of tracking prey within visible range. |
| **Pursuit** | Predator behavior of chasing prey to capture. |
| **Catch** | Event when predator and prey occupy the same map location. |
| **Tick** | Single discrete time step in the simulation. |
| **CSV** | Comma-Separated Values file format for data export. |
| **Unit Test** | Automated test of individual class or method functionality. |
| **Test Suite** | Collection of unit tests run together to validate system. |

---

**Document Status:** This PRD is based on repository evidence from class implementations, test files, and project structure. All claims are traceable to source files. Gaps marked "To Be Completed" require clarification from project stakeholders.
