"""
Elevator Project:
- Provide code that simulates an elevator. You are free to use any language.
Upload the completed project to GitHub (public) for discussion during interview.
- Document all assumptions and any features that weren't implemented.
- The result should be an executable, or script, that can be run with the following inputs and generate the following outputs.
    Inputs: [list of floors to visit] (e.g. elevator start=12 floor=2,9,1,32)
    Outputs: [total travel time, floors visited in order] (e.g. 560 12,2,9,1,32)
    Program Constants: Single floor travel time: 10
"""

import sys

from PySide6.QtWidgets import QApplication

from ui import ElevatorUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ElevatorUi()
    window.show()
    sys.exit(app.exec())
