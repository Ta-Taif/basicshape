
import unittest

from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(10, 20)

    def test_valid_construction(self):
        self.assertEqual(self.rect.length, 10)
        self.assertEqual(self.rect.width, 20)

    def test_initial_area(self):
        self.assertAlmostEqual(self.rect.area, 200)

    def test_zero_dimension_rejected(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, 0)

    def test_negative_dimension_rejected(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 5)
        with self.assertRaises(ValueError):
            Rectangle(5, -1)

    def test_nonnumeric_dimension_rejected(self):
        with self.assertRaises(TypeError):
            Rectangle("ten", 5)
        with self.assertRaises(TypeError):
            Rectangle(5, None)

    def test_length_change_recalculates_area(self):
        self.rect.length = 15
        self.assertAlmostEqual(self.rect.area, 300)

    def test_width_change_recalculates_area(self):
        self.rect.width = 5
        self.assertAlmostEqual(self.rect.area, 50)

    def test_failed_length_assignment_preserves_state(self):
        with self.assertRaises(ValueError):
            self.rect.length = -4
        self.assertEqual(self.rect.length, 10)
        self.assertAlmostEqual(self.rect.area, 200)

    def test_failed_width_assignment_preserves_state(self):
        with self.assertRaises(TypeError):
            self.rect.width = "wide"
        self.assertEqual(self.rect.width, 20)
        self.assertAlmostEqual(self.rect.area, 200)

    def test_default_and_custom_name(self):
        self.assertEqual(self.rect.name, "Rectangle")
        self.assertEqual(Rectangle(1, 2, "Door").name, "Door")


if __name__ == "__main__":
    unittest.main()
