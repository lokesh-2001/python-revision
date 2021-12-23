# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 

n = int(input("Enter a number: "))
li = list(range(1,n+1))
result = []
for i in li:
    if(n % i==0):
        result.append(i)
print(result)
