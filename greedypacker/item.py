"""
2D Item class.
"""


class Item:
    """
    Items class for rectangles inserted into sheets
    """

    def __init__(self, id, name, width, height,
                 CornerPoint: tuple = (0, 0),
                 rotation: bool = True) -> None:
        self.id = id
        self.name = name
        self.width = width
        self.height = height
        self.x = CornerPoint[0]
        self.y = CornerPoint[1]
        self.area = self.width * self.height
        self.rotated = False

    def __repr__(self):
        return f"<{self.name}: (id={self.id}, width={self.width}, height={self.height}, x={self.x}, y={self.y})>"

    def rotate(self) -> None:
        self.width, self.height = self.height, self.width
        self.rotated = False if self.rotated == True else True
