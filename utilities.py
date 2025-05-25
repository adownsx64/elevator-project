class Utilities:
    """
    A class to determine elevator movement and calculate travel time.
    """

    @staticmethod
    def simulate_elevator(floors_to_visit: list[int], start_floor: int = 1):
        """
        Simulate elevator movement.

        Parameters:
            `floors_to_visit` (list of int): The floors the elevator should visit in order.
            `start_floor` (int): The starting floor of the elevator (default: 1).

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
                total_time += abs(floor - current_floor) * 10
                current_floor = floor
                visited_floors.append(current_floor)
        return total_time, visited_floors
