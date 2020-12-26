import random
from typing import List
import numpy as np

import greedypacker

from model.vegetable import Vegetable
from model.garden_proposal import GardenProposal


def get_proposal(width: int,
                 height: int,
                 vegetables: List[Vegetable],
                 ) -> GardenProposal:

    # Making sure the garden is not a single point or empty
    assert width >= 2 and height >= 2
    # TODO: We can reimplement our own heuristic and packing_algo depending on customer needs.
    garden = greedypacker.BinManager(width, height, sorting=False, pack_algo='shelf',
                                     heuristic='best_width_fit', rotation=True)
    random.shuffle(vegetables)

    for v in vegetables:
        garden.add_items(greedypacker.Item(v.id, v.name, v.shape_width, v.shape_height))

    garden.execute()
    # garden.bins[0] : We take only the first bin as we have only 1 field to grow veggies
    return GardenProposal(width, height, vegetables, garden.bins[0].items)


def get_proposals(width: int,
                  height: int,
                  vegetables: List[Vegetable],
                  nb_proposals: int
                  ) -> List[GardenProposal]:
    return [get_proposal(width, height, vegetables) for i in range(nb_proposals)]


if __name__ == "__main__":
    veggies = Vegetable.get_vegetables()
    proposal = get_proposals(15, 5, veggies, nb_proposals=5)
    [print("\nProposal "+str(i)+":\n", p.__repr__()[1:]) for i, p in enumerate(proposal)]
