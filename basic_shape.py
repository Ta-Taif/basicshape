
from abc import ABC, abstractmethod


class BasicShape(ABC):


    def __init__(self, name):

        self._name = None
        self._area = 0.0
        self.name = name  # goes through the validating setter

    @property
    def name(self):

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
        return self._area

    @abstractmethod
    def calc_area(self):
        ...

    @staticmethod
    def _check_number(value, label):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{label} must be a number")
        return value

    @staticmethod
    def _check_positive(value, label):

        BasicShape._check_number(value, label)
        if value <= 0:
            raise ValueError(f"{label} must be greater than zero")
        return value
