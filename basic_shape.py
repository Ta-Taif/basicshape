"""Define the BasicShape abstract base class for the basic-shapes hierarchy."""

from abc import ABC, abstractmethod


class BasicShape(ABC):
    """Abstract base class (formal interface) for every shape.

    BasicShape stores a name and the most recently calculated area.
    Concrete subclasses must implement calc_area(), so an incomplete
    shape class can never be instantiated.
    """

    def __init__(self, name):
        """Initialize the shape's name and set the initial area to 0.0.

        The area is not calculated here because BasicShape does not know
        any subclass-specific dimensions.

        Args:
            name: A nonempty string labeling the shape.

        Raises:
            TypeError: If name is not a string.
            ValueError: If name is empty or only whitespace.
        """
        self._name = None
        self._area = 0.0
        self.name = name  # goes through the validating setter

    @property
    def name(self):
        """str: The shape's label. Must be a nonempty string.

        Raises:
            TypeError: If assigned a non-string.
            ValueError: If assigned an empty or whitespace-only string.
        """
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value.strip():
            raise ValueError("name must not be empty")
        self._name = value

    @property
    def area(self):
        """float: The current area. Read-only; updated by calc_area()."""
        return self._area

    @abstractmethod
    def calc_area(self):
        """Calculate the area, store it in the protected area attribute,
        and return it. Every concrete shape must implement or inherit this.
        """
        ...

    # ---- shared validation helpers used by subclasses ----
    @staticmethod
    def _check_number(value, label):
        """Return value if it is a real number (bool excluded), else TypeError."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{label} must be a number")
        return value

    @staticmethod
    def _check_positive(value, label):
        """Return value if it is a number greater than zero.

        Raises:
            TypeError: If value is not numeric.
            ValueError: If value is zero or negative.
        """
        BasicShape._check_number(value, label)
        if value <= 0:
            raise ValueError(f"{label} must be greater than zero")
        return value
