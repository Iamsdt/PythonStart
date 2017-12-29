li = [1, 2, 3, 4, 5, 6, 7, 8]

# print list
print("List:")
print(li)

# reverse list
print("\n\nreverse list")
li.reverse()
print(li)

# sort list
print("\n\nsort list")
li.sort()
print(li)

# add new element
print("\n\nadd new element: 9")
li.append(9)
print(li)

# insert new element
print("\n\nInsert new element")
li.insert(0, 0)
print(li)

# extend list
print("\n\nExtend List")
print("New List")
li2 = range(10, 21)
print(li2)

print("\nExtend Previous List")
li.extend(li2)
print(li)


