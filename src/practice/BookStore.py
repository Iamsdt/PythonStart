books = ["c", "java", "c++", "kotlin", "python", "swift", "c#"]

studentRate = 0.3
teacherRate = 0.2


def match_book(s):
    return books.__contains__(s)


def calculate(rate, price):
    temp = price * rate
    price = price - temp
    show(price)


def show(price):
    print("Your payable price is: " + str(price) + " Tk.")


print("*********  Welcome to our bookstore  *******")
b = input("Book name:")
if match_book(b.lower()):
    print("yes! we have " + b + " book")
    print("Price is 200 TK")
    ans = input("Are you Student or Teacher?")
    if ans.lower() == "student":
        calculate(studentRate, 200)
    elif ans.lower() == "teacher":
        calculate(teacherRate, 200)
    else:
        calculate(0.1, 200)

print("Thank you for shopping!")
