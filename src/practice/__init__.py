def user_input():
    return int(input("Enter number: "))


def prime(upper):
    count = 0
    for num in range(0, upper + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                count += 1

    print("Total Counted: " + str(count))
    run_again()


def run_again():
    print("Want to calculate again?")
    ans = str(input("Answer:"))
    if ans.lower() == "yes":
        prime(user_input())
    else:
        print("Thank you")


print("Welcome to our program")
prime(user_input())
