# 0 1 1 2 3 5 8 13 21 34 ...
def recur(n):
    if n <= 1:
        return n
    else:
        return recur(n - 1) + recur(n - 2)


print("How many terms?")
terms = int(input("Answer:"))

if terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(recur(i), end=" ")
