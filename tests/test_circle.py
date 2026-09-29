"""Unit tests for the Circle class."""

import math
import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(1, 2, 4)

    def test_valid_construction(self):
        self.assertEqual(self.circle.x_center, 1)
        self.assertEqual(self.circle.y_center, 2)
        self.assertEqual(self.circle.radius, 4)

    def test_initial_area(self):
        self.assertAlmostEqual(self.circle.area, math.pi * 16)

    def test_zero_radius_raises_value_error(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)

    def test_negative_radius_raises_value_error(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -3)

    def test_nonnumeric_radius_raises_type_error(self):
        with self.assertRaises(TypeError):
            Circle(0, 0, "big")

    def test_nonnumeric_center_raises_type_error(self):
        with self.assertRaises(TypeError):
            Circle("a", 0, 1)

    def test_radius_change_recalculates_area(self):
        self.circle.radius = 8
        self.assertAlmostEqual(self.circle.area, math.pi * 64)

    def test_coordinate_change_does_not_change_area(self):
        before = self.circle.area
        self.circle.x_center = -50
        self.circle.y_center = 0
        self.assertAlmostEqual(self.circle.area, before)

    def test_negative_and_zero_coordinates_allowed(self):
        circle = Circle(-5, 0, 1)
        self.assertEqual(circle.x_center, -5)
        self.assertEqual(circle.y_center, 0)

    def test_failed_radius_assignment_preserves_state(self):
        old_area = self.circle.area
        with self.assertRaises(ValueError):
            self.circle.radius = -1
        self.assertEqual(self.circle.radius, 4)
        self.assertAlmostEqual(self.circle.area, old_area)

    def test_default_name(self):
        self.assertEqual(self.circle.name, "Circle")

    def test_custom_name(self):
        self.assertEqual(Circle(0, 0, 1, "Wheel").name, "Wheel")


if __name__ == "__main__":
    unittest.main()
