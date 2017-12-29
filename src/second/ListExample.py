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

# Count a element occurrence
print("\nCount a element occurrence")
print(li.count(9))

# remove a element
# a costly operation
print("\nRemove a element")
li.remove(0)
print(li)

# pop function
print("\n\nPop function")
li.pop()
print(li)

# pop from index
print("Pop from index")
li.pop(0)
print(li)


# some fun
print("\n\nSome fun")
print("create a list with one hundred zero")
li = [0] * 100
print(li)

print("\n\n copy a list")
li2 = [1, 2, 3, 4, 5, 6, 7, 8]
print("List 2 ", li2)
li = li2
print("List 1:", li)

print("Change List 2")
li2[0] = 0
print("List 2:", li2)
print("List 1:", li)

# can not copy the list
# because it copy only the reference of a list
# if one change other will be changed




