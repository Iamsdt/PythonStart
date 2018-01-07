class BookStore:
    books =["c", "java", "c++", "kotlin", "python", "swift", "c#"]
    def match_book(self,s):
        return self.books.__contains__(s)
