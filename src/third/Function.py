def add(_a, _b):
    return _a + _b


print("Add two number")


# a = int(input())
# b = int(input())

# c = add(a, b)

# print("Result: ", c)

# pass value and parameter

def la(_a, _li):
    print("Type of first parameter: ", type(_a))
    print("Type of second parameter: ", type(_li))
    _li.append(_a)

    return _a


a = 10
myLi = list(range(0, 10))
print("My list: ", myLi)

y = la(a, myLi)
print("Return data: ", y)
print("value of a:", a)
print("value of my list:", myLi)

la(11, myLi)
print("value of a:", a)
print("value of my list:", myLi)


# set default value on function
def add3number(_a, _b, _c=0):
    return _a + _b + _c


c = add3number(1, 2)
d = add3number(1, 3, 4)
print("Add 3 number: ", c)
print("Add 3 number: ", d)


# return multiple value
def multiple(_a, _b, _c):
    _a += 10
    _b += 30
    _c += 20
    return _a, _b, _c


# receive
m = multiple(1, 2, 3)
print("Multiple value: ", m)
print("type: ", type(m))

print("length:", len(m))
print("1st value: ", m[0])

x, y, z = multiple(10, 20, 30)
print("\nvalue of x:", x)
print("value of y:", y)
print("value of z:", z)

# unpack tuple
a, b, c = m
print("\nvalue of a:", a)
print("value of b:", b)
print("value of c:", c)
print("Multiple value: ", m)


# default value and multiple value return
def suggest(n1, n2=None, n3=None, n4=None):
    li = [n1]

    if n2 is not None:
        li.append(n2)

    if n3 is not None:
        li.append(n3)

    if n4 is not None:
        li.append(n4)

    return li


def add_name():
    print("Please suggest some name:")
    return input()


def input_name(_a):
    print("Add more or skip")
    _b = input()
    if _b.lower() != "skip":
        print("Add name:")
        return input()
    else:
        print("Name Suggestions")
        _sug = suggest(_a)
        for _item in _sug:
            print(_item)
        exit()


a = add_name()
b = input_name(a)
print("Name Suggestions")
sug = suggest(a, b)
for item in sug:
    print(item)
