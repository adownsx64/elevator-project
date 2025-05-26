# elevator-project - Andrew Downs

## Description
This application is an interactive elevator simulator that allows users to model and visualize the movement of an elevator between floors. It is implemented in Python and provides a graphical user interface using `PySide6` and a set of utilities for simulating elevator travel logic.

# Installation Instructions

A binary executable for Windows-based computers is provided inside of the `dist` folder that can be ran directly without having to install Python. Otherwise, continue reading for installation instructions.

## Prerequisites
Ensure you have Python 3.11.3 or higher installed on your system. You can download it from [python.org](https://www.python.org/).

## Required Packages
The following Python package is required to run the project:
- `PySide6`

The following Python package is optional but is recommended for running the unit tests:
- `pytest`

## Installation Steps
1. **Clone the repository:**

    Open a terminal or command prompt, navigate to the directory where you want to place the project and run the clone command using git:

        git clone https://github.com/adownsx64/elevator-project.git

    Once the repository is done being cloned, navigate into the repository folder:

        cd elevator-project

2. **Create and activate a virtual environment (optional but recommended):**

    - On Windows:
        ```
        python -m venv myenv
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        python -m venv myenv
        source venv/bin/activate
        ```

3. **Install the required packages:**

    ```
    python -m pip install -r requirements.txt
    ```

4. **Run the application from base repository directory:**

    ```
    python start.py
    ```

5. **Run test suite from base repository directory (optional but recommended):**

    ```
    python -m pytest ./tests/test_utilities.py
    ```

## Usage
A user launches the application, enters the starting floor and a comma-separated list of floors to visit and clicks "Simulate Elevator." The application then displays the total travel time in seconds and the sequence of floors visited, helping users understand the efficiency of different elevator routes.