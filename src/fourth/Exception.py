from src.third.Calculator import div

print("Input first number:")
a = input()
print("Input second number:")
b = input()

try:
    c = div(int(a), int(b))
    print("Result:", c)
except ZeroDivisionError:
    print("you can not divided by zero")
except ValueError:
    print("Please input integer only!!!")
finally:
    print("thank you")

print("\nAnother program")
try:
    c = div(int(a), int(b))
except ValueError as e:
    print("Something went wrong")
else:
    print(c)
finally:
    print("thank you")

