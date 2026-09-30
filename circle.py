
import math

from basic_shape import BasicShape


class Circle(BasicShape):


    def __init__(self, x_center, y_center, radius, name="Circle"):

        super().__init__(name)
        self._x_center = 0
        self._y_center = 0
        self._radius = None
        self.x_center = x_center
        self.y_center = y_center

        self.radius = radius

    @property
    def x_center(self):
        return self._x_center

    @x_center.setter
    def x_center(self, value):
        self._x_center = self._check_number(value, "x_center")

    @property
    def y_center(self):
        return self._y_center

    @y_center.setter
    def y_center(self, value):
        self._y_center = self._check_number(value, "y_center")

    @property
    def radius(self):

        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = self._check_positive(value, "radius")
        self.calc_area()

    def calc_area(self):
        self._area = math.pi * self._radius ** 2
        return self._area
