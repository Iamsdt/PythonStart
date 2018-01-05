import src.third.Calculator as Cal
import src.third.Constant as Con


print("Input a number")
a = int(input())
print("Input another number")
b = int(input())

c = Cal.add(a, b)
print("\nAddition: ", c)

d = Cal.sub(a, b)
print("Sub: ", d)

e = Cal.mul(a, b)
print("Multiplication: ", e)

f = Cal.div(a, b)
print("Div: ", f)

print("Value of PI:", Con.PI)
