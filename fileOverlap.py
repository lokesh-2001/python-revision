# Given two .txt files that have lists of numbers in them, find 
# the numbers that are overlapping. One .txt file has a list of 
# all prime numbers under 1000, and the other .txt file has a 
# list of happy numbers up to 1000.

def overlap(fileName):
    li = []
    with open(fileName) as f:
        line = int(f.readline())
        while line:
            li.append(line)
            line = f.readline()
    return li

prime = overlap('primeNumbers.txt')
happy = overlap('happyNumbers.txt')

overlapList = [elem for elem in prime if elem in happy]
print(overlapList)
