class WrongNodeTypeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class DuplicateNodeException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class NodeNotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class WrongNodeIdException(Exception):
    def __init__(self):
        pass