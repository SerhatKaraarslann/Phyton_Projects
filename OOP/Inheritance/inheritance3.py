class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person object has been created!")

    def  intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self,name,surname, age,number): # We have to initialize this parameter in init method of parent class.
        Person.__init__(self, name,surname,age) # Because of this method a person object has been created before print on next line.
        self.number = number
        print("Student object has been created.") 

    def  intro(self): # if i have the same method in child class and call this method, it will be called this method not the method in base class.
        print(self.name, self.surname, self.age , self.number)

    def study(self):
        print(f"The student with number {self.number} studies now.")

    

p1 = Person("Serhat","Karaarslan",30)  
p1.intro()

s1 = Student("Markus","Rashford",28,101) 
s1.intro()
s1.study()

class Teacher(Person):
    def __init__(self, name,surname, age,branch):
        #Person.__init__(self,name,surname,age)
        super().__init__(name,surname,age) # I can use super() instead of parent class name. So i dont need call self in parameters too.
        self.branch = branch
        print("Teacher object has been created!")

    def teach(self):
        print(f"{self.name} {self.surname} teaches in {self.branch} branch!")

t1 = Teacher("Patrick","Stalljohann", 47,"Architecture of Software Systems") 
t1.intro()
t1.teach()