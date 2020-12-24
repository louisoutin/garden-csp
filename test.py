carrot = {
    "shape_id": 1,
    "shape_width": 4,
    "shape_height": 2
}

tomato = {
    "shape_id": 2,
    "shape_width": 5,
    "shape_height": 3
}

vegetables = [
    {},
    carrot,  # carrot id: 1
    tomato  # tomato id: 2
]


def init_matrix(cols, rows):
    arr = [[0] * cols] * rows
    return arr


def display_matrix(arr):
    for row in arr:
        for col in row:
            print(col, end=" ")
        print()


def place_shape(arr, id, top_left_i, top_left_j):
    shape_width = vegetables[id]["shape_width"]
    shape_height = vegetables[id]["shape_height"]
    print(shape_width, shape_height)
    for i in range(top_left_i, top_left_i + shape_width):
        for j in range(top_left_j, top_left_j + shape_height):
            arr[i][j] = id


width = 20
height = 10
garden = init_matrix(width, height)
display_matrix(garden)
print()
place_shape(garden, 1, 0, 0)
display_matrix(garden)
