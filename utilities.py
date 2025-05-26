"""
This module provides a utility class for simulating the elevator movement.

Attributes:
-----------
    `single_floor_travel_time`:
        The time it takes in seconds for the elevator to travel between two adjacent floors.

Functions:
----------
    `Utilities.simulate_elevator(floors_to_visit, start_floor=1)`:
        Calculates the total travel time and sequence of floors visited based upon the
        specified floors to visit as well as the starting floor.
"""


class Utilities:
    """A utility class to simulate elevator movement."""

    single_floor_travel_time = 10  # time in seconds to travel between two adjacent floors

    @staticmethod
    def simulate_elevator(
        floors_to_visit: list[int], start_floor: int = 1
    ) -> tuple[int, list[int]]:
        """
        Simulates the elevator movement based on the floors to visit and the starting floor.

        Parameters:
            `floors_to_visit` (list[int]): The floors the elevator will visit in order.
            `start_floor` (int, optional): The starting floor of the elevator. Default is 1.

        Returns:
            tuple[int, list[int]]:
                - total_time (int): Total travel time in seconds.
                - visited_floors (list[int]): The sequence of floors visited, including the start.
        """
        if not floors_to_visit:
            return 0, [start_floor]

        current_floor = start_floor
        visited_floors = [current_floor]
        total_time = 0

        for floor in floors_to_visit:
            if floor != current_floor:
                total_time += (
                    abs(floor - current_floor) * Utilities.single_floor_travel_time
                )
                current_floor = floor
                visited_floors.append(current_floor)

        return total_time, visited_floors
