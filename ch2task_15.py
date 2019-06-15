#For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascenddef 

def number ():
    x=int(input ("Enrer a number"))
    for num in range(1,x+1):
        if num**2<=x:
            print(num)
number()

