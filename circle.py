"""Define the Circle class for the basic-shapes hierarchy."""

import math

from basic_shape import BasicShape


class Circle(BasicShape):
    """A circle with a center point and a radius; inherits from BasicShape.

    Invariant: radius is always positive and area always equals
    pi * radius ** 2.
    """

    def __init__(self, x_center, y_center, radius, name="Circle"):
        """Create a Circle.

        Args:
            x_center: Numeric x-coordinate of the center.
            y_center: Numeric y-coordinate of the center.
            radius: Numeric radius greater than zero.
            name: Optional label, defaults to "Circle".
        """
        super().__init__(name)
        self._x_center = 0
        self._y_center = 0
        self._radius = None
        self.x_center = x_center
        self.y_center = y_center
        # Radius is validated and stored by its setter, which then calls
        # calc_area(), so area is only computed after a valid radius exists.
        self.radius = radius

    @property
    def x_center(self):
        """float: x-coordinate of the center. Any number; TypeError otherwise."""
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        self._x_center = self._check_number(value, "x_center")

    @property
    def y_center(self):
        """float: y-coordinate of the center. Any number; TypeError otherwise."""
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        self._y_center = self._check_number(value, "y_center")

    @property
    def radius(self):
        """float: The radius. Must be a number greater than zero.

        Assigning a valid value recalculates the area automatically.

        Raises:
            TypeError: If not numeric.
            ValueError: If zero or negative.
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        # Validate first so a failed assignment leaves the old state intact.
        self._radius = self._check_positive(value, "radius")
        self.calc_area()

    def calc_area(self):
        """Calculate, store, and return pi * radius squared."""
        self._area = math.pi * self._radius ** 2
        return self._area
