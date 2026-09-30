
from rectangle import Rectangle


class Square(Rectangle):
 
    def __init__(self, side, name="Square"):
    
        self._side = None
    
        super().__init__(side, side, name)

    @property
    def side(self):
      
        return self._side

    @side.setter
    def side(self, value):
        value = self._check_positive(value, "side")
        self._side = self._length = self._width = value
        self.calc_area()

    @Rectangle.length.setter
    def length(self, value):
        self.side = value

    @Rectangle.width.setter
    def width(self, value):
        self.side = value
