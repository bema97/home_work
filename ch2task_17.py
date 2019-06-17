a=[1,2,3,4,5,6,8,9,10]
b=[]
for integer in range(10):
    if integer not in a:
        b.append(integer)
        print (b)