dt = {'a': 'b', 'b': 'c'}

print(dt)

# access
print(dt['a'])

# insert non mutable value only
li = [1, 2, 3, 4, 5]
dt = {'li': li}
print(dt["li"])

# add and delete
del dt["li"]
print("\n", dt)

dt["name"] = "Shudipto"

print(dt)

dt["last"] = "Trafder"

print(dt)

# Run loop
print("\nLoop run...")
print("\n only keys")
for item in dt:
    print(item)

print("\n keys with value")
for item in dt:
    print(item, dt[item])

print("\nKeys with keys() function")
for item in dt.keys():
    print(item)

# key value
print("key value")
for key, value in dt.items():
    print(key, ":", value)

for x in dt.items():
    print(x)