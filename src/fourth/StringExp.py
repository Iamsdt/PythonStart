a = "Shudipto, Trafder"
b = a.split(",")
c = a.split()
print("with parameter:", b, "\nSize:", len(b))
print("without parameter:", c, "\nSize:", len(c))

# join
li = ['a', 'b', 'c', 'd']
b = ','.join(li)
c = '+'.join(li)
d = ''.join(li)

print("\njoin with comma", b)
print("join with plus", c)
print("join", d)

# problem: add plus sign after every char.
# input is abcdef
# output will be a+b+c+d+e+f
s = "abcdef"
li = list(s)
c = "+".join(li)
print(c)

# left right justified
for i in range(0, 15):
    print(i)

# but make those output to right justified
print("\n\n")
for i in range(0, 15):
    s = str(i).rjust(2)
    print(s)

print('100'.rjust(10))
print('10000'.rjust(10))

# String format
print('\nString format')
s = '{} vs {}'.format("Bangladesh", "Sri Lanka")
s1 = '{1} vs {0}'.format("Bangladesh", "Sri Lanka")
print(s)
print(s1)
