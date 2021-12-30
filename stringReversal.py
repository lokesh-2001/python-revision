# Ask the user for a string and print out whether this string is a palindrome or not.
wd =str(input("string : "))
rvs = wd[::-1]
if(rvs == wd):
    print("True")
else:
    print("False")
