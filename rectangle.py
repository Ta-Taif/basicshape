"""Define the Rectangle class for the basic-shapes hierarchy."""

from basic_shape import BasicShape


class Rectangle(BasicShape):
    """A rectangle with a length and width; inherits from BasicShape.

    Invariant: length and width are always positive and area always equals
    length * width.
    """

    def __init__(self, length, width, name="Rectangle"):
        """Create a Rectangle.

        Args:
            length: Numeric length greater than zero.
            width: Numeric width greater than zero.
            name: Optional label, defaults to "Rectangle".
        """
        super().__init__(name)
        # Both start as None so calc_area() can skip until both exist.
        self._length = None
        self._width = None
        self.length = length
        self.width = width

    @property
    def length(self):
        """float: The length. Must be a number greater than zero.

        Assigning a valid value recalculates the area automatically.

        Raises:
            TypeError: If not numeric.
            ValueError: If zero or negative.
        """
        return self._length

    @length.setter
    def length(self, value):
        self._length = self._check_positive(value, "length")
        self.calc_area()

    @property
    def width(self):
        """float: The width. Must be a number greater than zero.

        Assigning a valid value recalculates the area automatically.

        Raises:
            TypeError: If not numeric.
            ValueError: If zero or negative.
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = self._check_positive(value, "width")
        self.calc_area()

    def calc_area(self):
        """Calculate, store, and return length times width.

        During construction, while only one dimension exists, the area is
        left unchanged instead of failing.
        """
        if self._length is not None and self._width is not None:
            self._area = self._length * self._width
        return self._area
