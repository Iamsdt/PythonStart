tp = (1, 2, 3, [1, 2, 3, 4])

print("Tuple:", tp)
print(type(tp))

print("Index: 3", tp[3])

# convert tuple to list

li = list(tp)
print("\nList: ", li)

print("\n\n")
# tuple pack
tp = 0, 1, 2, 3
print(tp)

print("\nUnpack tuple")
a, b, c, d = tp
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# Create tuple with single element
t = (1)
print(type(t))

t = (1,)
print(type(t))

# use loop in tuple
for item in tp:
    print(item)

# Difference between tuple and list
# tuple is immutable
# list is mutable
