"""
This module contains the entry point for the Elevator Simulator user interface.

Initializes the Qt application event loop and displays the main Elevator Simulator user interface.
"""

import sys

from PySide6.QtWidgets import QApplication

from ui import ElevatorSimulatorUi

app = QApplication(sys.argv)
window = ElevatorSimulatorUi()
window.show()
sys.exit(app.exec())
