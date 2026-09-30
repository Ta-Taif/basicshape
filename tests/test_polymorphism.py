
import math
import unittest

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestPolymorphism(unittest.TestCase):
    def setUp(self):
        self.shapes = [
            Circle(0, 0, 2),
            Circle(1, 1, 3),
            Rectangle(4, 5),
            Rectangle(2, 6),
            Square(4),
        ]
        self.expected = [
            math.pi * 4,
            math.pi * 9,
            20,
            12,
            16,
        ]

    def test_all_are_basic_shapes(self):
        for shape in self.shapes:
            self.assertIsInstance(shape, BasicShape)

    def test_common_name_and_area_accessible(self):
        for shape in self.shapes:
            self.assertIsInstance(shape.name, str)
            self.assertGreater(shape.area, 0)

    def test_each_reports_correct_area(self):
        for shape, expected in zip(self.shapes, self.expected):
            self.assertAlmostEqual(shape.area, expected)

    def test_calc_area_through_common_interface(self):
        for shape, expected in zip(self.shapes, self.expected):
            self.assertAlmostEqual(shape.calc_area(), expected)


if __name__ == "__main__":
    unittest.main()
