def insert(x,y):
    return x[:int(len(x)/2)]+y+x[int(-len(x)/2):]
print(insert("[[]]",'Python'))
print(insert("{{}}",'PHP'))