"""
This is the liveness module
"""
from flask import jsonify


def is_alive():
    return jsonify({"status": "UP"})
