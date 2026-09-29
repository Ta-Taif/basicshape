"""Unit tests for the Square class."""

import unittest

from rectangle import Rectangle
from square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_valid_construction_is_synchronized(self):
        self.assertEqual(self.square.side, 5)
        self.assertEqual(self.square.length, 5)
        self.assertEqual(self.square.width, 5)

    def test_initial_area(self):
        self.assertAlmostEqual(self.square.area, 25)

    def test_is_a_rectangle(self):
        self.assertIsInstance(self.square, Rectangle)

    def test_side_change_keeps_everything_synchronized(self):
        self.square.side = 9
        self.assertEqual(self.square.length, 9)
        self.assertEqual(self.square.width, 9)
        self.assertAlmostEqual(self.square.area, 81)

    def test_length_assignment_preserves_invariant(self):
        self.square.length = 7
        self.assertEqual(self.square.side, 7)
        self.assertEqual(self.square.width, 7)
        self.assertAlmostEqual(self.square.area, 49)

    def test_width_assignment_preserves_invariant(self):
        self.square.width = 3
        self.assertEqual(self.square.side, 3)
        self.assertEqual(self.square.length, 3)
        self.assertAlmostEqual(self.square.area, 9)

    def test_invalid_sides_rejected(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-2)
        with self.assertRaises(TypeError):
            Square("five")

    def test_failed_side_assignment_preserves_state(self):
        with self.assertRaises(ValueError):
            self.square.side = -1
        self.assertEqual((self.square.side, self.square.length, self.square.width), (5, 5, 5))
        self.assertAlmostEqual(self.square.area, 25)

    def test_failed_length_assignment_preserves_state(self):
        with self.assertRaises(ValueError):
            self.square.length = 0
        self.assertEqual((self.square.side, self.square.length, self.square.width), (5, 5, 5))
        self.assertAlmostEqual(self.square.area, 25)

    def test_default_and_custom_name(self):
        self.assertEqual(self.square.name, "Square")
        self.assertEqual(Square(2, "Tile").name, "Tile")


if __name__ == "__main__":
    unittest.main()
