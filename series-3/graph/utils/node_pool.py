from .node import Node

class NodePool:
    def __init__(self):
        self._pool = dict()

    def add_vertice(self, vertice:Node):
        if vertice is None:
            raise Exception("There is no Node to be added")

        if vertice.id in self._pool:
            raise Exception("There is a Duplicate Node!")

        self._pool = vertice

    def get_vertice(self, id:str):
        if id not in self._pool:
            return None

        return self._pool[id]