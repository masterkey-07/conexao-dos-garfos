class WrongNodeTypeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class DuplicateNodeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class NodeNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class WrongNodeIdError(Exception):
    def __init__(self):
        pass