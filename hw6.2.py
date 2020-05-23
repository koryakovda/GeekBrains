class Road:
    def __init__(self,_lenth,_width):
        self._lenth = _lenth
        self._width = _width
    def mass(self):
        a = self._lenth*self._width*25*0.05
        print(a)
a = Road(5000,20)
a.mass()
print(a._lenth)