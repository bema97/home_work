string = "Bermet"

#exercise 1

print (string[2])

#exercese 2
print (string[4])

#exercise 3
print (string[:4]) 

#exercise 4
print (string[:3]) 

#exercise 5

for n,letters in enumerate(string):
     if n % 2==1:
          print(letters)
     
#exercise 6

for i,letters in enumerate (string):
     if i % 2==0:
          print(letters)
     
#exercise 7

print (string[::-1])

#exercise 8

for i,letters in enumerate (string[::-1]):
     if i % 2==0:
          print (letters)






