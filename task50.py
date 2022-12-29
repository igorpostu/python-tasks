class Circle:
    def __init__(self, radius: int, color: str) -> None:
        self._radius = radius
        self._color = color
        
    def _get_color(self) -> str:
        print("Get color")
        return self._color
    
    def _set_color(self, color: str) -> None:
        print("Set color")
        self._color = color
    
    def _del_color(self) -> None:
        print("Delete color")
        del self._color
    
    color = property(_get_color, _set_color, _del_color)
    
    @property
    def radius(self) -> int:
        print("Get radius")
        return self._radius

    @radius.setter
    def _set_radius(self, value: int) -> None:
        print("Set radius")
        self._radius = value

    @radius.deleter
    def radius(self) -> None:
        print("Delete radius")
        del self._radius