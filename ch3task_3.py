list=[]
n=int(input("Enter your quality:"))
for i in range (n):
    k = int(input("Enter your number: "))
    list.append(k)
    
a= int(input("enter a number: "))
if a<0:
    list.reverse()
for i in range(abs(a)):
    list.append(list[i])
    del(list[i])
if a<0:
    list.reverse()
print(list)