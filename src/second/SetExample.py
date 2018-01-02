
a = set()

# type
print(type(a))

# insert data
# can't take single value
# must insert value by using iterable
tpl = (1, 2, 3)
a = set(tpl)
print("Set:", a)

li = [1, 2, 3, 4, 5, 6, 7]
b = set(li)
print("\nSet b: ", b)

# A and B
print("\nA intersection b: ", a & b)
print("A union b: ", a | b)

# test a element is on set
print("\n", 7 in a)
print(7 in b)

# create a set by using string
c = set("abcd")
print("\nSet:c ", c)

# uses of set
# remove duplicate value from list
li = [1, 2, 3, 4, 5, 6, 7, 5, 6, 7, 3, 3, 4, 5, 7]
print(li)
d = set(li)
print(d)
# convert to list again
li = list(set(li))
print("List after set: ", li)

# set comprehension


