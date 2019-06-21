text=(input('Please, write any text: '))
lower=upper=0
letter=(len(text))

for i in text:
    if "a"<=i<="z":
        lower +=1
    elif "A"<=i<="Z":
        upper +=1


print("the letters % is"%(lower/letter*100))
print("the letters % is"%(upper/letter*100))