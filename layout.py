"""
This is the layout module
"""
from constraint import *
from flask import jsonify
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('layout')

problem = Problem()


def recommend(specification):
    logger.info('entering recommend with user input: %s', specification)
    return jsonify({})
