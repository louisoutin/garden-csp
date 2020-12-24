"""
This is the layout module
"""
from flask import jsonify
from garden_solver import *
import logging

from model.garden import Garden

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('layout')

gardenSolver = GardenSolver()


def recommend(specification):
    logger.info('entering recommend with user input: %s', specification)
    vegetables = specification["vegetables_inventory"]["vegetables"]
    logger.info('available vegetables: %s', vegetables)
    garden = Garden(specification["garden"]["width"], specification["garden"]["height"])
    garden.print()
    all_solutions = gardenSolver.solve()
    solutions = []

    for solution in all_solutions:
        if len(solutions) >= specification["wanted_proposals"]:
            break
        solutions.append(solution)

    return jsonify({"solutions": solutions})
