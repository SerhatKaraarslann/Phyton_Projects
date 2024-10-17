class Person:
    #Constructor
    def __init__(self,name,surname, year):
       #Object attributes
        self.name = name
        self.surname = surname
        self.year = year

    #instance methods
    def intro(self):
        return f"My name is {self.name} {self.surname}"
    
    def calculate_age(self):
        return f"{2024 - self.year}"

#Object, Instance
person1 = Person("Serhat","Karaarslan",1994)
person2 = Person("Julia","Penner",1997)

print(person1.intro())
print(person2.intro())

print(person2.calculate_age())
