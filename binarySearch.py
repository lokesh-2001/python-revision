def binarySearch(li,si,ei, x):
    if ei>si:
        mi = int((si+ei)/2)
        # if(mi < 0  or mi < si or mi>ei):
        #     return False
        if li[mi] > x:
            return binarySearch(li,si,mi-1,x)
        elif li[mi] == x:
            return True
        return binarySearch(li,mi+1,ei,x)
    return False
l = [2,4,5,7,8,9]
print(binarySearch(l,0,len(l)-1,1))
print(binarySearch(l,0,len(l)-1,2))
print(binarySearch(l,0,len(l)-1,3))
print(binarySearch(l,0,len(l)-1,4))
print(binarySearch(l,0,len(l)-1,5))
print(binarySearch(l,0,len(l)-1,6))