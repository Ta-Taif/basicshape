"""Define the Square class for the basic-shapes hierarchy."""

from rectangle import Rectangle


class Square(Rectangle):
    """A square; inherits from Rectangle (multilevel from BasicShape).

    Invariant: side, length, and width are always equal, so Rectangle's
    calc_area() (length * width) is reused unchanged.
    """

    def __init__(self, side, name="Square"):
        """Create a Square.

        Args:
            side: Numeric side length greater than zero.
            name: Optional label, defaults to "Square".
        """
        self._side = None
        # Rectangle.__init__ assigns length and width, which our overridden
        # setters route to the side property.
        super().__init__(side, side, name)

    @property
    def side(self):
        """float: The side length. Must be a number greater than zero.

        Assigning a valid value updates side, length, width, and area
        together, so the square can never become inconsistent.

        Raises:
            TypeError: If not numeric.
            ValueError: If zero or negative.
        """
        return self._side

    @side.setter
    def side(self, value):
        value = self._check_positive(value, "side")
        # Update everything only after validation succeeds.
        self._side = self._length = self._width = value
        self.calc_area()

    # Design choice: assigning length or width changes the whole square.
    @Rectangle.length.setter
    def length(self, value):
        self.side = value

    @Rectangle.width.setter
    def width(self, value):
        self.side = value
