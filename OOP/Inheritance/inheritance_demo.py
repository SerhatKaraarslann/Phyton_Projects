#User class as a base class.
#Moderator class inherits the base class and adds some extras in itself.

class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        if(cls.active_users == 1 or cls.active_users == 0):
            return f"Right now {cls.active_users} user is active."
        return f"Right now {cls.active_users} users are active."

    def __init__(self, firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def fullname(self):
        return(f"{self.firstname} {self.lastname}")
    
    


class Moderator(User):

    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        if(cls.active_moderators == 1 or cls.active_moderators == 0):
            return f"Right now {cls.active_moderators} moderator is active"
        return f"Right now {cls.active_moderators} moderators are active"

    def __init__(self, firstname, lastname, community):
        super().__init__(firstname,lastname)
        self.community = community
        Moderator.active_moderators += 1

    def remove_post(self):
        return f"{self.fullname()} in the {self.community} group removed a post."

    
    def update_post(self):
        return f"{self.fullname()} in the {self.community} group updated a post."

print(User.display_active_users()) # 0
print(Moderator.display_active_moderators()) # 0
u1 = User("Jack","Sparrow")
m1 = Moderator("Davy","Jones","Hollanders")
print(User.display_active_users()) #2
print(Moderator.display_active_moderators()) #1

m2 = Moderator("Will", "Turner","Swords")
print(User.display_active_users()) #3
print(Moderator.display_active_moderators()) #2
print(Moderator.display_active_users())#3 # We can call this method in child class too.

print(isinstance(u1,User)) # The method, which return true or false due to type of instance, True is here. u1 is a User.
print(isinstance(u1,Moderator)) #False

print(isinstance(m1,User)) # True, Modearotar inherits User class.
print(isinstance(m1, Moderator)) # True

print(u1.fullname()) # Jack Sparrow
print(m1.fullname()) # Davy Jones

print(m1.remove_post())

print(m2.update_post())