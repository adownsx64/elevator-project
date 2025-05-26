"""
This module contains the entry point for the Elevator Project user interface.

Initializes the Qt application event loop and displays the main Elevator UI window.
"""

import sys

from PySide6.QtWidgets import QApplication

from ui import ElevatorUi

app = QApplication(sys.argv)
window = ElevatorUi()
window.show()
sys.exit(app.exec())
