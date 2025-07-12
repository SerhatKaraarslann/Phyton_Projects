class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object has been created!")

    def  intro(self):
        print(self.name, self.name, self.age)


class Student(Person): # Thats for inheritance. Without inheritance I create this class just with bracket, however with inheritance i have to write the parent class in this bracket.
    pass

p1 = Person("Serhat","Karaarslan",30)  # Person object has been created.
#print(p1.name, p1.surname, p1.age)
p1.intro()
s1 = Student("Markus","Rashford",28) #Now i created with inheritance a Student object from Person class. 
#print(s1.name, s1.surname,s1.age)
s1.intro()

class Teacher(Person):
    pass

t1 = Teacher("Patrick","Stalljohann", 47) # Teacher is a person too. like student.
#print(t1.name,t1.surname,t1.age)
t1.intro()