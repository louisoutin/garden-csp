import json


class Vegetable():

    def __init__(self, id, name, shape_width, shape_height):
        self.id = id
        self.name = name
        self.shape_width = shape_width
        self.shape_height = shape_height

    def __repr__(self):
        return f"<name : {self.name} / id: {self.id} / width: {self.shape_width} / height: {self.shape_height}>\n"

    @staticmethod
    def get_vegetable_list(path: str = "../list_vegetables.json"):
        res = []
        with open(path) as f:
            data = json.load(f)
        for v in data["vegetables"]:
            v_obj = Vegetable(v["id"], v["name"], v["shape_width"], v["shape_height"])
            res.append(v_obj)
        return res

    @staticmethod
    def get_vegetable_list_by_id(path: str = "../list_vegetables.json"):
        res = {}
        with open(path) as f:
            data = json.load(f)
        for v in data["vegetables"]:
            v_obj = Vegetable(v["id"], v["name"], v["shape_width"], v["shape_height"])
            res[v["id"]] = v_obj
        return res
