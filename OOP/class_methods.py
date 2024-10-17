class User: 
    #the attributes, which not in initmethod defined, in class
    active_users = 0
    
    #Class methods are called with class name and return cls and take cls as a parameter
    @classmethod
    def displayActiveUsers(cls):
        return f"{cls.active_users} users active!"
    
    #with this method we can create an object from class
    @classmethod
    def from_string(cls,data_str):
        name,lastname,age = data_str.split(",")
        return cls(name,lastname,age)


    def __init__(self,name,lastname,age):
        print(self)
        self.name = name
        self.lastname = lastname
        self.age = age
        # we call this class attribute with class name
        User.active_users +=1 
    

    def full_name(self):
        return f"{self.name} {self.lastname}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} not active."

print(User.displayActiveUsers())
userA = User("Serhat","Karaarslan","30")
userB = User("Julia","Penner",27)    
print(User.displayActiveUsers())

print(userB.logout())
print(User.displayActiveUsers())

print(userA.full_name())
print(userB.full_name())


ferhat = User.from_string("Ferhat,Karaarslan,34")
print(ferhat.age)

#if we create a dictionary instance we re doing this but with dict.fromkeys() method from dict class we can also create an instance
#{"key" : "value"}
#dict.fromkeys()