words=(input("Please, enter any words: "))

list_1=words.split()

list_1.sort(key=len)
list_1=" ".join(list_1)
print(list_1)