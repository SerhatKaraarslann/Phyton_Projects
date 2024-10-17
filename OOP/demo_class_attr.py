class Pet:
    genders = ["cat","dog","bird"]
    def __init__(self,name, gender):
        if gender not in Pet.genders:
            raise ValueError(f"{gender} is not a pet!")
        self.name = name
        self.gender = gender

boncuk = Pet("Boncuk","cat")
pasha =  Pet("Pasha","dog")
mavis = Pet("Mavis","bird")

#pars = Pet("Pars","lion")  #ValueError: lion is not a pet!

Pet.genders.append("fish") #we can add a new gender in class attribute
boncuk.genders.append("sheep") # with boncuk instnce we can add a attribute too

print(Pet.genders)
print(boncuk.genders)
print(pasha.genders)