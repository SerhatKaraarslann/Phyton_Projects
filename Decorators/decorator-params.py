# Thats the normal using of decorators

def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice

@do_twice
def hello():
    print("Hello!")

# Now if i wanna give to my function a parameter 
# it cant working. I have to give the parameter in decorater function too.
# This time i have problem with the function, which has no parameters.
# Because of that i have to use *args and **kwargs

@do_twice
def greet(msg):
    print("Hello "+msg)

# They work now.
hello()
greet("World!")

@do_twice
# if my function return a value, i have to return in the decorator too.
# return func(*args,**kwargs)
def return_greeting(name):
    print("Greeting function ")
    return f"Hello, {name}"

print(return_greeting("Serhat"))