from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, x_move, y_move):
        obj = deepcopy(self)
        obj.move(x_move, y_move)
        return obj
