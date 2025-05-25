from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QWidget,
    QSizePolicy,
    QSpacerItem,
)

from utilities import Utilities


class ElevatorUi(QWidget):
    """A class to build the elevator simulation UI using PySide6."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elevator Simulator")
        self.setMinimumWidth(370)
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        layout = QGridLayout()

        self.value_start_floor = QSpinBox()
        self.value_start_floor.setMinimum(1)
        layout.addWidget(QLabel("Start Floor:"), 0, 0)
        layout.addWidget(self.value_start_floor, 0, 1)

        self.input_floors_visited = QLineEdit()
        self.input_floors_visited.setPlaceholderText(
            "Enter floors to visit (comma separated)"
        )
        # Regex for input validation, ensuring only digits and commas are allowed.
        regex = QRegularExpression(r"^\d+(,\d+)*$")
        validator = QRegularExpressionValidator(regex)
        self.input_floors_visited.setValidator(validator)
        layout.addWidget(QLabel("Floors to Visit:"), 1, 0)
        layout.addWidget(self.input_floors_visited, 1, 1)

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

    def slot_btn_simulate_elevator(self):
        """Simulate the elevator based on user input."""
        if not self.input_floors_visited.hasAcceptableInput():
            return

        start_floor = self.value_start_floor.value()
        floors = [int(floor) for floor in self.input_floors_visited.text().split(",")]
        total_travel_time, floors_visited = Utilities.simulate_elevator(
            floors, start_floor
        )
        self.value_total_travel_time.setText(f"{total_travel_time} seconds")
        self.value_floors_visited.setText(", ".join(map(str, floors_visited)))
