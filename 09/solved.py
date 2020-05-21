str=input("Add something: ")
new_str=""
for i in range (len(str)):
    if i%2==0:
        continue
    new_str +=str[i]
print(new_str)