s = "a, b, c, d"

li = s.split(",")

print("Split with only ',' ")
for i in li:
    print(i)

print("\nSplit with only space' ' ")
li = s.split(" ")

for i in li:
    print(i)

print("\nSplit with space and comma ', ' ")
li = s.split(", ")
for i in li:
    print(i)

# now join
print("Join with nothing")
s = ''.join(li)
print(s)

print("Join with plus")
s = '+'.join(li)
print(s)

print("Join with coma")
s = ','.join(li)
print(s)

print("\njustify")

s = "Data"
print("Right justify:" + s.rjust(10) + ":")
print("Left justify:" + s.ljust(10) + ":")
print("Center justify:" + s.center(10) + ":")

print("\nFormat")
vs = "{0} vs {1}".format("Bangladesh", "Sri Lanka")
print(vs)

print("\nFormat without index")
vs = "{} vs {}".format("Bangladesh", "Sri Lanka")
print(vs)

print("\nFormat with name")
vs = "{team1} vs {team2}".format(team1="Bangladesh", team2="Sri Lanka")
print(vs)

