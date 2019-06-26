s1=(input('Enter any words: '))
s2=(input('Enter any words: '))
full_string=s1+s2
set_letters=set(full_string)
q_letters=len(set_letters)
q_letters2=len(full_string)
a= int(q_letters)
b=int(q_letters2)
print(q_letters)
print(q_letters2)

if a==b:
    print('NO')
elif a!=b:
    print("YES")

