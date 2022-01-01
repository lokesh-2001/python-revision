def max3(a,b,c):
    max = 0
    if a>b:
        if a>c:
            max = c
        else:
            max = a
    else:
        if b>c:
            max = b
        else:
            max = c
    return max
print(max3(1,2,3))