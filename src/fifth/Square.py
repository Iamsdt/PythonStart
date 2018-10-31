class Square:
    def __init__(self):
        self.side = 0

    def area(self):
        return self.side * self.side


# this is called instantiation
sq = Square()
sq.side = 5
area = sq.area()
print(area)


# this is called attribute reference
# a = Square.side


class Square2:
    def __init__(self, x):
        self.side = x

    def area(self):
        return self.side * self.side


sq = Square2(5)
area = sq.area()
print(area)
