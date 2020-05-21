import random
l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]
l3=l1+l2
def rand_element():
    return random.choice(l3)
def second_smallest():
    l3.sort()
    return l3[1]
def second_largest():
    l3.sort()
    return l3[len(l3)-2]

print(rand_element())
print(second_smallest())
print(second_largest())