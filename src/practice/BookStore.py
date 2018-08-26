books = ["c", "java", "kotlin", "dart", "python"]
student = 0.3
teacher = 0.2
occupation = ""


def search(name):
    return books.__contains__(name)


def calculate(answer):
    total = 200
    if answer == "student":
        money = total - (total * student)
        return money
    elif answer == "teacher":
        money = total - (total * teacher)
        return money
    else:
        return total


def run_again():
    print("\nWant more book?")
    answer = str(input("Answer:"))
    if answer.lower() == "yes":
        print("\n")
        cus()
    else:
        print("Thank you")


def cus():
    print("Which book do you want?")
    user = str(input("Answer:"))

    # search
    status = search(user.lower())

    # check status
    if status:
        print("\nWe have " + user + " book")
        print("Price is 200 tk.")
        if occupation.__len__() == 0:
            print("\nWhat is your occupation?")
            occupation.__add__(str(input("Answer:")))
            print(occupation)

        price = calculate(occupation.lower())
        print("\nYour total payable price is " + str(price) + " tk")
        run_again()
    else:
        print("Thank you")


print("Welcome to our book store")
cus()
