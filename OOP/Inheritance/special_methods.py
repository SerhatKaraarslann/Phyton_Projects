list = [1,2,3,4,5]

print(len(list))

s = "Serhat Karaarslan"

print(len(s))

#This special method len is speical and descriebt in this class like list and string class.
#We can specialize this kind of special methods in our classes.

class Film:
    def __init__(self, titel, regisseur, time):
        self.titel = titel
        self.regisseur = regisseur
        self.time = time

    def __str__(self):
        return f"{self.titel} was directed by {self.regisseur}."
    
    def __repr__(self):
        return f"{self.titel} was directed by {self.regisseur}."
    
    def __len__(self):
        return self.time
    

    def __del__(self):
        print("This movie object has been deleted.")


f = Film("The Lord Of The Rings:  Two Towers", "Peter Jackson", 198)
print(str(f)) # The Lord Of The Rings:  Two Towers was directed by Peter Jackson.
print(repr(f)) # The Lord Of The Rings:  Two Towers was directed by Peter Jackson.
print(f) # print(str(f)) # The Lord Of The Rings:  Two Towers was directed by Peter Jackson.

print(len(f)) # special len method due to my description in this class. #198

del f # Our del function , #This movie object has been deleted.