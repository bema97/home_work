#about files

hello=input('say "Hello": ')
print (hello)

countries = ['1) google_kazakstan.txt', '2)google_paris.txt', 
'3)google_uar.txt', '4)google_kyrgystan.txt', '5)google_san_francisco.txt', 
'6) google_germany.txt', '7)google_moscow.txt', '8)google_sweden.txt']
complain = input("youre text")

question = input("Whats your country?: ")

if question:
    with open(countries[int(question)-1], 'a') as f:
        f.write(complain)