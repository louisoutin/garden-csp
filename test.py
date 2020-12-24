from model.garden import Garden
from model.vegetable_dictionnary import vegetable_shapes, carrot, tomato

garden = Garden(20, 10)
garden.print()
garden.place_shape(carrot, 0, 0)
garden.place_shape(tomato, 5, 4)
garden.place_shape(tomato, 10, 7)
print()
garden.print()
