import sys

# userCommand = int(input())
# prime_number = 0
# for num in range(2, userCommand):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         s = str(num) + ' '
#         sys.stdout.write(s)
#         prime_number += 1


# while True:
#     i = int(input())
#
#     if i == 42:
#         break
#     else:
#         print(i)

# print("\n\n")
# print("Total Prime number in range 0 to",userCommand,":",prime_number)

#s = input()
#print(s[::-1])

i = int(input())
j = 0
while i > 0:
    p = int(input())
    i -= 1
    if p >= 0:
        j += p

print(j)