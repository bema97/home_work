
# Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2. 


name=str(input('enter a word that have "f"'))

if name.count('f') == 1:
    print(-1)
elif name.count('f') < 1:
    print(-2)
else:
    print(name.find('f', name.find('f') + 1))