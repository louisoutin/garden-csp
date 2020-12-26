from typing import List

import numpy as np
import greedypacker
from model.vegetable import Vegetable


class GardenProposal:

    def __init__(self,
                 width,
                 height,
                 vegetables_availables: List[Vegetable],
                 vegetables_position: List[greedypacker.Item]
                 ):
        self.width = width
        self.height = height
        self.vegetables_availables = vegetables_availables
        self.vegetables_position = vegetables_position
        self.vegetables_unused = self._get_vegetables_unused()
        self.garden = np.zeros((width, height))
        self._fill_garden()

    def _get_vegetables_unused(self) -> List[Vegetable]:
        used_veggies_ids = [v.id for v in self.vegetables_position]
        return [v for v in self.vegetables_availables if v.id not in used_veggies_ids]

    def _fill_garden(self):
        for v in self.vegetables_position:
            x_left = v.x
            x_right = v.x + v.width
            y_top = v.y
            y_bottom = v.y + v.height
            rect = np.ones((v.width, v.height)) * v.id
            self.garden[x_left:x_right, y_top:y_bottom] = rect

    def __repr__(self) -> str:
        return np.array2string(self.garden) + f" \n Unusued Vegetables : {self.vegetables_unused}"
