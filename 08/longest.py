def longest(l):
    size=0
    for i in l:
        if len(i)>=size:
            size=len(i)
            word=i
    return word

print(longest(['banana','apple','lemon','watermelon']))