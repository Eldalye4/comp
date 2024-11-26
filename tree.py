class Node:
    def __init__(self, type, children=None, leaf=None):
        self.type = type
        self.children = children if children else []
        self.leaf = leaf

class BinOp(Node):
    def __init__(self, left, op, right):
        super().__init__("binop", [left, right], op)

class Number(Node):
    def __init__(self, value):
        super().__init__("number", None, value)
