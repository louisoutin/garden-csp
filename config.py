"""
This is the config module
"""
from flask import jsonify


def read():
    """
    This function responds to a request for /config
    with the application configuration
    :return:        json string representing the configuration
    """
    return jsonify({"config": {}})
