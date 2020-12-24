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
    return jsonify({"solutions": gardenSolver.solve()})
