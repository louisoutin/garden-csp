import numpy as np

from model.vegetable_dictionnary import vegetable_shapes
from util.array import display_matrix


class Garden:
    garden_matrix = None
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.garden_matrix = np.zeros((height, width), dtype=np.uint8)

    def print(self):
        #print(self.garden_matrix)
        display_matrix(self.garden_matrix, self.width, self.height)

    def place_shape(self, shape_id, top_left_i, top_left_j):
        shape_width = vegetable_shapes[shape_id]["shape_width"]
        shape_height = vegetable_shapes[shape_id]["shape_height"]
        for i in range(top_left_i, top_left_i + shape_width):
            for j in range(top_left_j, top_left_j + shape_height):
                self.garden_matrix[j][i] = shape_id
