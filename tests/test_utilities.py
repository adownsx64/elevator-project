"""
Unit tests for the `Utilities` class, which provides a method to simulate elevator movement.

To run the tests, execute this module directly or use a test runner like `pytest`.
"""

from unittest import TestCase, main

from utilities import Utilities


class TestUtilities(TestCase):
    """Test suite for the `Utilities` class."""

    def test_simulate_elevator_no_floors(self):
        """Test the `simulate_elevator()` function with no floors to visit."""
        total_time, visited = Utilities.simulate_elevator([])
        assert total_time == 0
        assert visited == [1]

    def test_simulate_elevator_single_floor(self):
        """Test the `simulate_elevator()` function with a single floor request."""
        total_time, visited = Utilities.simulate_elevator([3])
        # 1 -> 3: 2 * 10 = 20, total = 20
        assert total_time == 20
        assert visited == [1, 3]

    def test_simulate_elevator_multiple_floors(self):
        """Test the `simulate_elevator()` function with multiple floor requests."""
        total_time, visited = Utilities.simulate_elevator([3, 5, 2])
        # 1 -> 3: 2 * 10 = 20, 3 -> 5: 2 * 10 = 20, 5 -> 2: 3 * 10 = 30, total = 70
        assert total_time == 70
        assert visited == [1, 3, 5, 2]

    def test_simulate_elevator_with_start_floor(self):
        """Test the `simulate_elevator()` function with a custom starting floor."""
        total_time, visited = Utilities.simulate_elevator([4, 2], start_floor=2)
        # 2 -> 4: 2 * 10 = 20, 4 -> 2: 2 * 10 = 20, total = 40
        assert total_time == 40
        assert visited == [2, 4, 2]

    def test_simulate_elevator_repeated_floors(self):
        """Test the `simulate_elevator()` function with repeated floor requests."""
        total_time, visited = Utilities.simulate_elevator([1, 1, 2, 2, 3])
        # 1 -> 2: 1 * 10 = 10, 2 -> 3: 1 * 10 = 10, total = 20
        assert total_time == 20
        assert visited == [1, 2, 3]

    def test_simulate_elevator_negative_floors(self):
        """Test the `simulate_elevator()` function with negative floor requests."""
        total_time, visited = Utilities.simulate_elevator([-1, -3])
        # 1 -> -1: 2 * 10 = 20, -1 -> -3: 2 * 10 = 20, total = 40
        assert total_time == 40
        assert visited == [1, -1, -3]

    def test_simulate_elevator_same_floor(self):
        """Test the `simulate_elevator()` function with requests to the same floor."""
        total_time, visited = Utilities.simulate_elevator([1, 1, 1])
        assert total_time == 0
        assert visited == [1]

    def test_simulate_elevator_zero_floor(self):
        """Test the `simulate_elevator()` function with zero as a floor request."""
        total_time, visited = Utilities.simulate_elevator([0])
        # 1 -> 0: 1 * 10 = 10
        assert total_time == 10
        assert visited == [1, 0]

    def test_simulate_elevator_negative_start_floor(self):
        """Test simulate_elevator() with a negative starting floor."""
        total_time, visited = Utilities.simulate_elevator([0, 2], start_floor=-2)
        # -2 -> 0: 2 * 10 = 20, 0 -> 2: 2 * 10 = 20, total = 40
        assert total_time == 40
        assert visited == [-2, 0, 2]

    def test_simulate_elevator_zero_start_floor(self):
        """Test simulate_elevator() with zero as the starting floor."""
        total_time, visited = Utilities.simulate_elevator([2, -2], start_floor=0)
        # 0 -> 2: 2 * 10 = 20, 2 -> -2: 4 * 10 = 40, total = 60
        assert total_time == 60
        assert visited == [0, 2, -2]

    def test_simulate_elevator_negative_and_zero_floors(self):
        """Test simulate_elevator() with negative and zero floors in the visit list."""
        total_time, visited = Utilities.simulate_elevator([-2, 0, -1], start_floor=-1)
        # -1 -> -2: 1 * 10 = 10, -2 -> 0: 2 * 10 = 20, 0 -> -1: 1 * 10 = 10, total = 40
        assert total_time == 40
        assert visited == [-1, -2, 0, -1]

    def test_simulate_elevator_all_same_negative_start(self):
        """Test simulate_elevator() with all requests to the same negative floor."""
        total_time, visited = Utilities.simulate_elevator([-3, -3, -3], start_floor=-3)
        assert total_time == 0
        assert visited == [-3]

    def test_simulate_elevator_empty_with_negative_start(self):
        """Test simulate_elevator() with no floors to visit and negative start."""
        total_time, visited = Utilities.simulate_elevator([], start_floor=-5)
        assert total_time == 0
        assert visited == [-5]


if __name__ == "__main__":
    main()
