"""
This is the layout module
"""
from flask import jsonify
from garden_solver import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('layout')

gardenSolver = GardenSolver()


def recommend(specification):
    logger.info('entering recommend with user input: %s', specification)
    all_solutions = gardenSolver.solve()
    print(all_solutions)
    solutions = []

    for solution in all_solutions:
        if len(solutions) >= specification["wanted_proposals"]:
            break
        solutions.append(solution)

    return jsonify({"solutions": solutions})
