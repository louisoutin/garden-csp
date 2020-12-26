import json
from typing import List


class Vegetable():

    def __init__(self,
                 id: int,
                 name: str,
                 shape_width: int,
                 shape_height: int):
        self.id = id
        self.name = name
        self.shape_width = shape_width
        self.shape_height = shape_height

    def __repr__(self) -> str:
        return f"<name : {self.name} / id: {self.id} / width: {self.shape_width} / height: {self.shape_height}>\n"

    @staticmethod
    def get_vegetables(path: str = "../list_vegetables.json") -> List['Vegetable']:
        res = []
        with open(path) as f:
            data = json.load(f)
        for v in data["vegetables"]:
            v_obj = Vegetable(v["id"], v["name"], v["shape_width"], v["shape_height"])
            res.append(v_obj)
        return res

    @staticmethod
    def get_vegetables_by_id(path: str = "../list_vegetables.json") -> dict:
        res = {}
        with open(path) as f:
            data = json.load(f)
        for v in data["vegetables"]:
            v_obj = Vegetable(v["id"], v["name"], v["shape_width"], v["shape_height"])
            res[v["id"]] = v_obj
        return res
