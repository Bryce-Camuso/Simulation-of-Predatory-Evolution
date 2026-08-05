# Final project set up

## File structure

| folder             | description                                                                         |
|--------------------|-------------------------------------------------------------------------------------|
| Home               | Holds simulation files, testing batch files, ReadMe, and git files                  |
| classes            | Holds the python class files used for this project                                  |
| csv                | Holds the data files from testing/final output                                      |
| documents          | Holds the documents related to the final theisis                                    |
| documents/archived | Holds the documents compleated throughout the project and related class submissions |

## Project Dependencies

- Python 3.14.4
- Python Sudo-Random Library (3.14.4)
- Python Standard Math Library (3.14.4)
- Python Heap queue algorithm [heapq] (3.14.4)
- Python Command-line parsing library [argparse] (3.14.4)
- Python Concurrent library (3.14.4)
- Python Pandas library (3.0.3)

## Getting Started

To begin running this project the user must have all dependencies listed above downloaded on their computer. 

To download these dependencies, go to [python.org/downloads](https://www.python.org/downloads/) and find the version [3.14.4](https://www.python.org/downloads/release/python-3144/).

From there, choose the correct download option for your operating system, and go through the installation process.

To confirm that python is downloaded and working correctly, you can use the command **python** or **python --version** in a terminal of your choice

The following dependencies will be included in the python download: Python Sudo-Random Library, Python Math Library, Python Heap queue algorithm, Python Command-line parsing library, Python Concurrent library.

The following dependencies will not be included in the python download: [Python Pandas library](https://pandas.pydata.org/).

To install the pandas library you can use the following command in a terminal of your choice **pip install pandas==3.0.3** 

## Running project files

To run any python script (denoted by a .py extension) in the project, use the command line to type **python \<filepath\> [args]** and hit enter. The program file should run automatically. 

e.g. **python classes/Scent.py** to run the Scent class tester. 

## Simulations versions

The simulation built in this project has been split into 4 diffrent versions for diffrent purposes. The table below contains the simulation version, it's file location, and the purposes. To run any of the simulations they **MUST BE IN THE HOME DIRECTORY** of the project. Note some versions of the simulation may require comand line arguments to be passed in. These are noted in the section [File Comand Line Arguments](#file-comand-line-arguments) section.

| File               | File Location      | Purpose                                                                           |
|--------------------|--------------------|-----------------------------------------------------------------------------------|
| simulation-test.py | documents/archived | This file is used to test the simulation to get detailed data on what happend at each phase of the simulation. |
| simulation-demo.py | documents/archived | This file acts as a demo for the project. It runs a small scale version of the simulation to show working status and sample outputs.|
| simulation-v1.py   | documents/archived | This file acts as the first version of the full simulation. It is used to run one on one testing with predators and prey. |
| simulation-v2.py   | home               | This file is the final version of the simulation. It runs all three prey items against a mix population of ambush and pursuit predators|

## File Comand Line Arguments

This section lists out any files that requrments. Before running a new file in the project please consult this section for required and optinal arguments. 

### simulation-test

Comand line: **python simulation-test.py \<predatorType\> \<preyType\> [-o file path]**

| name         |flag or position | extended flag | defult value      | valid arguments         | description                                                     |
|--------------|-----------------|---------------|-------------------|-------------------------|-----------------------------------------------------------------|
| predatorType | position = 1    | N/A           | required argument | Ambush \| Pursuit       | What predator is being tested                                   |
| preyType     | position = 2    | N/A           | required argument | Rabbit \| Mouse \| Bird | What prey is being tested                                       |
| output       | -o              | --output      | stdout            | Valid file path         | Redirects the standard output into the designated file location |

### simulation-demo (WIP)

Comand line: **python simulation-demo.py \<predatorType\> \<preyType\> [-o file path]**

| name         |flag or position | extended flag | defult value      | valid arguments         | description                                                     |
|--------------|-----------------|---------------|-------------------|-------------------------|-----------------------------------------------------------------|
| predatorType | position = 1    | N/A           | required argument | Ambush \| Pursuit       | What predator is being tested                                   |
| preyType     | position = 2    | N/A           | required argument | Rabbit \| Mouse \| Bird | What prey is being tested                                       |
| output       | -o              | --output      | stdout            | Valid file path         | Redirects the standard output into the designated file location |

### simulation-v1

Comand line: **python simulation-v1.py \<predatorType\> \<preyType\> [-o file path] [-sp int] [-g int] [-sm int] [-em int]**

| name                | flag or position | extended flag        | defult value      | valid arguments         | description                                                     |
|---------------------|------------------|----------------------|-------------------|-------------------------|-----------------------------------------------------------------|
| predatorType        | position = 1     | N/A                  | required argument | Ambush \| Pursuit       | What predator is being tested                                   |
| preyType            | position = 2     | N/A                  | required argument | Rabbit \| Mouse \| Bird | What prey is being tested                                       |
| output              | -o               | --output             | csv/output.csv    | Valid file path         | Redirects the standard output into the designated file location |
| starting population | -sp              | --startingPopulation | 10000             | int >= 1                | Sets the starting population size (how many predators are in generation 0) |
| generation          | -g               | --generation         | 1000              | int >= 0                | Sets how many generations the simulation will go through |
| starting max        | -sm              | --startingMax        | 5000              | int >= 1                | Sets the maximum for population size at the start (how many predators are allowed after generation 0) |
| ending max          | -em              | --endingMax          | 500               | int >= 1                | Sets the maximum for population size at the end (how many predators are allowed in the final generation) |


