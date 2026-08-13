# Product Requirements Document

**Predator-Prey Simulation System**

---

# Cover Page

- **Project Name:** Predator-Prey Simulation System
- **Student(s):** Bryce Camuso
- **Course:** CISC 699
- **Semester:** Summer 2026
- **Repository URL:** [github](https://github.com/Bryce-Camuso/Simulation-of-Predatory-Evolution)
- **Current Branch:** master
- **Current Commit SHA:** 92220e7
- **Current Release Version:** 2.0
- **Document Version:** 0.5
- **Last Updated:** 2026-08-12

---

# Revision History

| Version | Date | Git Commit | Description | Author |
|----------|------|------------|-------------|--------|
| 0.1 | 2026-07-21 | test PRD | Initial PRD scaffold created from prompt structure. | Bryce Camuso |
| 0.2 | 2026-07-21 | PRD update with prompts | Updated PRD based on repository evidence: predator-prey simulation with scent tracking, map-based navigation, and multiple animal types. | Bryce Camuso |
| 0.3 | 2026-07-25 | PRD manual update | Updated PRD to better reflect the projects intentions that have not been reflected in code yet. | Bryce Camuso |
| 0.4 | 2026-08-05 | 6b846f4 | Updated PRD to align scope, features, and testing with the current repository implementation. | Bryce Camuso |
| 0.5 | 2026-08-12 | 92220e7 | Updated PRD to reflect current repository evidence, final version labeling, and metadata. | GitHub Copilot |

---

- **Related configuration management report:** `documents/CONFIGURATION_MANAGEMENT_REPORT.md`

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

- **Version 0.1:** Initial prototype with animal classes, map, scent system, and simulation drivers.
- **Version 1.0:** Intermediate refinement of behavior modeling, validation logic, and simulation support.
- **Version 2.0:** Final version delivered by this repository snapshot, including the `simulation-v2.py` evolutionary driver and CSV export.

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

# 4. Observed Artifacts and Limitations

- Inline `tester()` functions are present in several modules under `classes/`.
- `simulation-v2.py` is the main evolutionary simulation driver with pandas CSV export.
- No formal `pytest`, `unittest`, or CI workflow is present in the repository snapshot.
- Runtime performance metrics and formal test results are not documented in the repository.

---

# 5. Functional Requirements

| Requirement ID | Description | Evidence Source |
|---------------|-------------|-----------------|
| FR-1 | The system shall initialize animal objects with speed, stealth, stamina, sense, and position. | `classes/Animal.py` |
| FR-2 | The system shall provide getters and setters for animal attributes and position. | `classes/Animal.py`, `classes/Bird.py`, `classes/Prey.py`, `classes/Rabbit.py` |
| FR-3 | The system shall maintain energy state and subtract energy based on animal actions. | `classes/Animal.py` |
| FR-4 | The system shall generate a 301×301 map grid and allow tile queries. | `classes/Map.py` |
| FR-5 | The system shall generate scent trails, update them, and decay scent intensity. | `classes/Scent.py`, `classes/Animal.py`, `classes/Plant.py` |
| FR-6 | The system shall support ambush and pursuit predator behavior. | `classes/Predator.py`, `simulation-v2.py` |
| FR-7 | The system shall support prey behavior including escape state and type-specific movement. | `classes/Prey.py`, `classes/Rabbit.py`, `classes/Bird.py` |
| FR-8 | The system shall export simulation results to CSV using pandas. | `simulation-v2.py` |
| FR-9 | The system shall accept command-line parameters in `simulation-v2.py`. | `simulation-v2.py` |

---

# 6. Quality Requirements

- The repository is structured as pure Python with a dependency on `pandas`.
- Code organization is class-based and includes inline smoke-test functions.
- No formal automated test framework or CI configuration is present.

---

# 7. Performance Requirements

- Performance characteristics and metrics are To Be Completed.

---

# 8. Assumptions

- Python 3.14.4 is the intended runtime environment.
- The map is a bounded discrete grid from 0 to 300 in both dimensions.
- Animals use discrete movement and scent trail mechanics.
- Simulation state is exported only via CSV, not a database.
- Formal automated testing and CI are not available in this repository snapshot.

---

# 9. Constraints

| Constraint | Value |
|------------|-------|
| Programming Language | Python 3.14.4 |
| Required Libraries | random, math, heapq, argparse, concurrent.futures, pandas |
| Framework | None (pure Python) |
| Persistence | CSV files only |
| External Services | None |

---

# 10. External Interfaces

## User Interfaces

- Command-line execution through `simulation-v2.py` and earlier simulation scripts.

## Software Interfaces

- Python module imports from `classes/`.
- CSV export via `pandas.DataFrame.to_csv()`.

## Hardware Interfaces

- Standard file I/O only.

## External Services

- None.

---

# 11. Requirements Traceability Matrix

| Requirement ID | Evidence Source |
|---------------|-----------------|
| FR-1 | `classes/Animal.py` |
| FR-2 | `classes/Animal.py`, `classes/Bird.py`, `classes/Prey.py`, `classes/Rabbit.py` |
| FR-3 | `classes/Animal.py` |
| FR-4 | `classes/Map.py` |
| FR-5 | `classes/Scent.py`, `classes/Animal.py`, `classes/Plant.py` |
| FR-6 | `classes/Predator.py`, `simulation-v2.py` |
| FR-7 | `classes/Prey.py`, `classes/Rabbit.py`, `classes/Bird.py` |
| FR-8 | `simulation-v2.py` |
| FR-9 | `simulation-v2.py` |

---

# 12. Future Versions

- **Version 0.1:** Initial prototype with animal classes, map, scent system, and simulation drivers.
- **Version 1.0:** Intermediate refinement of behavior modeling and validation support.
- **Version 2.0:** Final version delivered by this repository snapshot.


---

# 13. Open Issues

- No formal issue list is provided in the repository.
- Formal performance and quality metrics are not documented.
- The repository does not include a CI workflow or automated test suite.

---

# 14. Glossary

| Term | Definition |
|------|-----------|
| Animal | Base class for moving simulation entities. |
| Predator | Animal subclass with hunting strategy and reproduction logic. |
| Prey | Animal subclass with evasion behavior and energy management. |
| Scent | Decaying environmental trail used for navigation. |
| Map | 2D grid environment with tile lookup. |
| Tile | Map cell type: Plain, Tree, or Bush. |
| CSV | Comma-Separated Values export format. |
| CLI | Command-line interface. |

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
| Simulation runtime for small test scenario | 500 simulation runs (500 iterations each): Ambush strategy averages 1.19 seconds; Pursuit strategy averages 1.27 seconds. Fastest: Pursuit + Rabbit = 0.94 seconds (467.96 seconds total). Slowest: Pursuit + Mouse = 1.87 seconds (932.53 seconds total). Overall average: 1.06 seconds per test run. |
| CSV export performance for production data | Simulation data with genetic information (50+ parents and 50+ offspring per run) exported to CSV format via pandas. Output includes predator type, prey type, success metrics (search, stalk, spot, phase 2, escape, catch rates), exhaustion rates, and complete genetic profiles (speed, stealth, stamina, sense attributes). Export completes within the total simulation time with no measurable overhead. |
| Memory usage per animal | Current implementation maintains 6 concurrent entities: 1 predator, 1 prey, and 4 plants. Each animal object stores: position (2 integers), attributes (speed, stealth, stamina, sense, energy: 5 integers each), and behavior state. Estimated per-animal memory: <1 KB for base entity, <2 KB per genetic record. |
| Maximum concurrent animals | Validated at 6 concurrent entities (1 predator + 1 prey + 4 plants) with stable performance. No formal scaling tests conducted for larger populations; scalability for 10+ animals is deferred to Version 3.0. |
| Scent trail decay computation | Scent trail updates occur during each simulation iteration within the 80-step movement cycle. Decay is computed per map location at fixed intervals (scentCountDownMax = 20 per cycle). No measurable performance degradation observed across 500 consecutive simulation runs. |
| Position calculation latency | Average per-iteration movement and position calculation: ~0.002 seconds per 80-step cycle (480 movement cycles per run ÷ avg 1.06 seconds = ~0.0022 seconds per cycle). Supports real-time pathfinding and position updates within the simulation constraint model. |

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
