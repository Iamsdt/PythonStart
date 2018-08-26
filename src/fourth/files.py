# Modes r- read mode
# Modes w- write mode
# Modes a- append mode
# Modes r+- read and write mode

file = "file.txt"
fp = open(file, "w")
fp.write("This is the first line\n")
fp.close()

# now add new line
fp = open(file, "a")
fp.write("This is the second line\n")
fp.close()

# now read
fp = open(file, "r")
print(fp.read())
# move back the pointer to the first
fp.seek(0)
print(fp.readlines())

print("\nwithout close")
with open(file, "r") as fp:
    print(fp.readline())

print(fp.closed)
