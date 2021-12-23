# Ask the user for a number. Depending on whether the number 
# is even or odd, print out an appropriate message to the user.

num = int(input("give a number to check: "))
check = int(input("give a number to divide by: "))

if(num%4==0):
    print(num , " is a multiple of 4 ")
elif(num%2==0):
    print(num , " is a even number ")
else:
    print(num," is an odd number")
 
if (num%check == 0 ):
    print("num divisible by the given number")
else:
    print("Not divisible")

