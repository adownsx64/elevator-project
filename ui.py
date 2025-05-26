"""
This module defines the `ElevatorSimulatorUi` class that builds up the user interface using `PySide6`.

Classes:
--------
    `ElevatorSimulatorUi`:
        A `QWidget` subclass that provides input fields for the starting floor, a list of floors
        to visit and displays the total travel time as well as the order of floors visited.

Functions:
----------
    `ElevatorSimulatorUi.__init__()`:
        Sets the window title, the window minimum width and calls the UI setup function.
    `ElevatorSimulatorUi.setup_ui()`:
        Sets up the individual UI components including input fields, labels and a button.
    `ElevatorSimulatorUi.slot_btn_simulate_elevator()`:
        Calls the `Utilities.simulate_elevator` function with the user input when the "Simulate
        Elevator" button is called and updates the UI with the results.
"""

from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QWidget,
)

from utilities import Utilities


class ElevatorSimulatorUi(QWidget):
    """A class to build the elevator simulator user interface using `PySide6`."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Elevator Simulator")
        self.setMinimumWidth(370)
        self.setup_ui()

    def setup_ui(self) -> None:
        """Setup the user interface components."""
        layout = QGridLayout()

        self.value_start_floor = QSpinBox()
        self.value_start_floor.setMinimum(1)
        layout.addWidget(QLabel("Start Floor:"), 0, 0)
        layout.addWidget(self.value_start_floor, 0, 1)

        self.input_floors_to_visit = QLineEdit()
        self.input_floors_to_visit.setPlaceholderText(
            "Enter floors to visit (comma separated)"
        )
        # Regex for input validation, ensuring only digits and commas are allowed.
        regex = QRegularExpression(r"^\d+(,\d+)*$")
        validator = QRegularExpressionValidator(regex)
        self.input_floors_to_visit.setValidator(validator)
        layout.addWidget(QLabel("Floors to Visit:"), 1, 0)
        layout.addWidget(self.input_floors_to_visit, 1, 1)

        self.label_total_travel_time = QLabel("Total Travel Time")
        self.value_total_travel_time = QLabel("--")
        self.label_floors_visited = QLabel("Floors Visited (in order)")
        self.value_floors_visited = QLabel("--")
        layout.addWidget(self.label_total_travel_time, 2, 0)
        layout.addWidget(self.value_total_travel_time, 2, 1)
        layout.addWidget(self.label_floors_visited, 3, 0)
        layout.addWidget(self.value_floors_visited, 3, 1)

        self.btn_simulate_elevator = QPushButton("Simulate Elevator")
        layout.addWidget(self.btn_simulate_elevator, 4, 0, 1, 2)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer, 5, 0)
        self.setLayout(layout)

        self.btn_simulate_elevator.clicked.connect(self.slot_btn_simulate_elevator)

    def slot_btn_simulate_elevator(self) -> None:
        """Simulate the elevator based on user input."""
        if self.input_floors_to_visit.text().endswith(","):
            self.input_floors_to_visit.setText(self.input_floors_to_visit.text()[:-1])

        if not self.input_floors_to_visit.hasAcceptableInput():
            return

        start_floor = self.value_start_floor.value()
        floors_to_visit = self.input_floors_to_visit.text()
        floors = [int(floor) for floor in floors_to_visit.split(",")]

        total_travel_time, floors_visited = Utilities.simulate_elevator(
            floors, start_floor
        )
        self.value_total_travel_time.setText(f"{total_travel_time} seconds")
        self.value_floors_visited.setText(", ".join(map(str, floors_visited)))
