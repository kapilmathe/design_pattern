class ShareInterface:
    def draw(self):
        pass


class Circle(ShareInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShareInterface):
    def draw(self):
        print("Square.draw")


class ShareFactory:
    @staticmethod
    def getShape(typ):
        if typ == 'circle':
            return Circle()
        if typ == 'square':
            return Square()
        assert 0, "Could not find the shape " + typ
