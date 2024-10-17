class User: 
    #the attributes, which not in initmethod defined, in class
    active_users = 0
    def __init__(self,name,lastname,age):
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

print(User.active_users)
userA = User("Serhat","Karaarslan","30")
userB = User("Julia","Penner",27)    
print(User.active_users)

print(userB.logout())
print(User.active_users)

print(userA.full_name())
print(userB.full_name())