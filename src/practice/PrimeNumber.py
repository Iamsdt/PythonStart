print("Input a integer number:")
userCommand = int(input())
print("\n\n")
print("Prime number start:")
prime_number = 0
for num in range(0,userCommand):
    if num > 0:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            prime_number += 1

print("\n\n")
print("Total Prime number in range 0 to",userCommand,":",prime_number)