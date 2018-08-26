print("Problems:1")
# Problems
# we have a string a, b, c, d, e
# Remove the white space and add plus sign
s = "a, b, c, d"
n = s.split(", ")
print(n)

li = "+".join(n)
print("New list")
print(li)

print("\n\n")
print("Problems:2")
# print a lit with right justify
# Add zero in empty space

for i in range(20):
    print(str(i).rjust(2))

print("\nFilled with zero")
for i in range(20):
    print(str(i).rjust(2, '0'))

print("\n\n")
print("Problems:3")
# print a lit with right justify
# Add zero in empty space
# Don't use justify
for i in range(20):
    print(str(i).zfill(2))

# Note you can use minus
print("\n\n")
print('12'.zfill(6))
print('-12'.zfill(6))