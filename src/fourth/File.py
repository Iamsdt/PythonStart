# working with Files steps
# Open
# read or write
# Close

# Mode for read and write
# r -> read
# w -> write
# a -> append means: you start to write on after existing
# r+ -> read and write

file = "test.txt"
fp = open(file, "w")
fp.write("Hello word!")
fp.close()

fp = open(file, 'a')
fp.write("\nI am learning python")
fp.close()

fp = open(file, 'r')
c = fp.read()
fp.close()
print(c)

fp = open(file, "a")
fp.write("\nThis is an awesome language")
fp.close()

print("\nRead:")
fp = open(file, 'r')
c = fp.read()
print(c)
print("\nRead line by line")
fp.seek(0)
li = fp.readlines()
print(li)
for line in li:
    print(line)

# open file another way
# no need to close
print("\n\n")
with open(file, 'r') as fp:
    print(fp.read())

print(fp.close())
