import numpy as np

carrot = 1
tomato = 2

carrot_shape = {
    "shape_id": carrot,
    "shape_width": 4,
    "shape_height": 2
}

tomato_shape = {
    "shape_id": tomato,
    "shape_width": 5,
    "shape_height": 3
}

vegetable_shapes = [
    {},
    carrot_shape,  # carrot id: 1
    tomato_shape  # tomato id: 2
]


def init_matrix(cols, rows):
    return np.zeros((rows, cols), dtype=np.uint8)


def display_matrix(arr, cols, rows):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end=" ")
        print()


def place_shape(arr, shape_id, top_left_i, top_left_j):
    shape_width = vegetable_shapes[shape_id]["shape_width"]
    shape_height = vegetable_shapes[shape_id]["shape_height"]
    for i in range(top_left_i, top_left_i + shape_width):
        for j in range(top_left_j, top_left_j + shape_height):
            arr[j][i] = shape_id


width = 20
height = 10
garden = init_matrix(width, height)
display_matrix(garden, width, height)
print()
place_shape(garden, carrot, 0, 0)
place_shape(garden, tomato, 0, 4)
place_shape(garden, tomato, 10, 7)

display_matrix(garden, width, height)
