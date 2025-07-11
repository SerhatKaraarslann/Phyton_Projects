class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object has been created!")

    def  intro(self):
        print(self.name, self.name, self.age)


class Student(Person):
    pass

p1 = Person("Serhat","Karaarslan",30)  
p1.intro()

s1 = Student("Markus","Rashford",28) 
s1.intro()

class Teacher(Person):
    pass

t1 = Teacher("Patrick","Stalljohann", 47) 
t1.intro()