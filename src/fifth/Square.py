class Square:
    side = 0

    def area(self):
        return self.side * self.side


sq = Square()
sq.side = 5
area = sq.area()
print(area)