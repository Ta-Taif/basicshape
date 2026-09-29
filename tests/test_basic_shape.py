"""Unit tests for the BasicShape abstract base class."""

import unittest

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle


class TestBasicShape(unittest.TestCase):
    def test_cannot_instantiate_directly(self):
        with self.assertRaises(TypeError):
            BasicShape("Shape")

    def test_subclass_missing_calc_area_cannot_instantiate(self):
        class Incomplete(BasicShape):
            pass

        with self.assertRaises(TypeError):
            Incomplete("Incomplete")

    def test_subclasses_inherit_name_and_area_interface(self):
        for shape in (Circle(0, 0, 1), Rectangle(2, 3)):
            self.assertIsInstance(shape, BasicShape)
            self.assertIsInstance(shape.name, str)
            self.assertGreater(shape.area, 0)

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 1, name="   ")

    def test_nonstring_name_rejected(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 1, name=42)

    def test_name_setter_updates_name(self):
        shape = Rectangle(1, 1)
        shape.name = "Box"
        self.assertEqual(shape.name, "Box")

    def test_area_is_read_only(self):
        shape = Circle(0, 0, 1)
        with self.assertRaises(AttributeError):
            shape.area = 99


if __name__ == "__main__":
    unittest.main()
