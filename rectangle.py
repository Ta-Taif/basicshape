
from basic_shape import BasicShape


class Rectangle(BasicShape):


    def __init__(self, length, width, name="Rectangle"):

        super().__init__(name)
        self._length = None
        self._width = None
        self.length = length
        self.width = width

    @property
    def length(self):
        self._length

    @length.setter
    def length(self, value):
        self._length = self._check_positive(value, "length")
        self.calc_area()

    @property
    def width(self):

        return self._width

    @width.setter
    def width(self, value):
        self._width = self._check_positive(value, "width")
        self.calc_area()

    def calc_area(self):

        if self._length is not None and self._width is not None:
            self._area = self._length * self._width
        return self._area
