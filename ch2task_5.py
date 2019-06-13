class_1=int(input('How many students?'))
class_2=int(input('How many students?'))
class_3=int(input('How many students?'))

students_all=[class_1,class_2,class_3]

all=int(sum(students_all))

left=all//2
if left %2==1:
    left+=1
print(left) 


    

        



