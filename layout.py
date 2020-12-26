"""
This is the layout module
"""
from flask import jsonify
import logging

from model.vegetable import Vegetable
from solver.greedy_solver import get_proposals

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('layout')


def recommend(specification):
    """
    Example request:
    {
        "garden": {
            "width": 5,
            "height": 3
        },
        "vegetables_inventory": {
            "vegetables": [1,2]
        },
        "wanted_proposals": 1
    }
    """
    logger.info('entering recommend with user input: %s', specification)
    input_vegetables = specification["vegetables_inventory"]["vegetables"]
    width = specification["garden"]["width"]
    height = specification["garden"]["height"]
    nb_proposals = specification["wanted_proposals"]
    logger.info('input vegetables: %s', input_vegetables)
    vegetables_knowledge = Vegetable.get_vegetables_by_id("./list_vegetables.json")
    inputs = []
    for input_veggie_id in input_vegetables:
        if input_veggie_id not in vegetables_knowledge.keys():
            return jsonify({f"error : unknown vegetable id : {input_veggie_id}"})
        veggie = vegetables_knowledge[input_veggie_id]
        inputs.append(veggie)

    # Calling the greedy algorithm resolution algorithm
    garden_proposals = get_proposals(width, height, inputs, nb_proposals)

    solutions = []
    for i, garden_proposal in enumerate(garden_proposals):

        layout = []
        for vegetable in garden_proposal.vegetables_position:
            layout.append({
                "id": vegetable.id,
                "name": vegetable.name,
                "x": vegetable.x,
                "y": vegetable.y,
                "width": vegetable.width,
                "height": vegetable.height
            })

        unused = []
        for vegetable in garden_proposal.vegetables_unused:
            unused.append({
                "id": vegetable.id,
                "name": vegetable.name,
                "width": vegetable.shape_width,
                "height": vegetable.shape_height,
            })

        solutions.append({
            "proposal_nb": (i+1),
            "layout": layout,
            "unusued_vegetables": unused
        })

    return jsonify({"solutions": solutions})
