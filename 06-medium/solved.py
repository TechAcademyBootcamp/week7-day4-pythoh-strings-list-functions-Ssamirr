color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
same=[]
for i in color1:
    for j in color2:
        if i==j:
            same.append(i)
print(same)