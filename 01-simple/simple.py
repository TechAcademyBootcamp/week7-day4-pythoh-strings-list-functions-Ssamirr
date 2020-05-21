def simple():
    count=5
    l=[]
    while count:
        count -=1
        val=int(input("Enter value: "))**2
        l.append(val)
    return l
    
print(simple())