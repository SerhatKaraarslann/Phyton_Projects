# Decorators are functions that modify the behavior of other functions,
# without changing their actual code
# A decorator takes a function as input, does something before or after that function runs, 
# and then returns a new function.

def morning():
    print("Good morning!")
   # print("My name is Serhat.")
   # print("Have a nice day!")

def day():
    print("Good day!")
  # print("My name is Serhat.")
  # print("Have a nice day!")
   
# In these two functions there are some blocks are same.
# We can write a function, which has contains the same blocks to make my codes clearer.
  
def greetings(fn):
    def wrapper():
        fn()
        print("My name ist Serhat.")
        print("have a nice day!")
    return wrapper


mor = greetings(morning)
mor()

d = greetings(day)
d()

# We can the code blocks, that we wanna call before or after a function,
# compact in a new function and call this function like greetings function.
# There is an another way to do it and it calls decorator.

# Now i wrote this function the same way.
# I dont need create an object like over to call this function.
# instead i wrote my function name with @ symbol before my function.

def greet(fn):
    def wrapper(name):
        print("Hi!")
        fn(name)
        print("What are you doing?")
    return wrapper

@greet
def callX(name):
    print("Hey you,", name)

@greet
def callY(name):
    print("Ach du,", name)

# Then i call my original function
callX("Serhat")
callY("Julia")

