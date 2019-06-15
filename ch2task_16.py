#Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()
numbers=[]
sis = int(input())
for x in range(sis):
    value = int (input())
    numbers.append(value)



for num in numbers:
    if num % 2 == 0:
        print (num)

