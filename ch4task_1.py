class Student:
    def __init__(self, name, lastname,department, year_of_entrance):
        self.name=name
        self.lastname=lastname
        self.year_of_entrance=year_of_entrance
        self.department=department
    def get_info(self):
        info=self.name.title() + self.lastname.title() + "postupil na " + self.year_of_entrance + " v " + self.department.title()
        return info

thestudent=Student('Vasya ','Ivanov ', '2017 ' ,' Programmirovanie')
print(thestudent.get_info())