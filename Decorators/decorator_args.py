# Till now we send the parameter just to the inner functions not direct to the decorators.
# Now we see how we can send the parameters to the decorators.
# This is called "Parametrized Decorators" or "Decorator Factory"

# This is a decorator factory - it creates decorators with custom parameters
# Structure: Outer function takes decorator parameters -> returns actual decorator -> decorator wraps function
def dec_do_twice(count):  # This function takes the parameter for the decorator
    def do_twice(func):   # This is the actual decorator that receives the function
        def wrapper_do_twice(*args,**kwargs):  # This is the wrapper that executes the function
            for _ in range(count):  # Use the 'count' parameter from outer function
                func(*args,**kwargs)
        return wrapper_do_twice
    return do_twice  # Return the decorator function

# Using the parametrized decorator with different count values
# @dec_do_twice(count = 5) means: call dec_do_twice(5) which returns a decorator
# Then that decorator is applied to the hello() function

@dec_do_twice(count = 5)  # This will make hello() run 5 times
def hello():
    print("Hello")

@dec_do_twice(count = 3)  # This will make greet() run 3 times  
def greet(name):
    print("Hello ",name)

# Testing our parametrized decorators
# hello() will print "Hello" 5 times because count=5
hello()

print("---")  # Separator for better output readability

# greet("Serhat") will print "Hello Serhat" 3 times because count=3
greet("Serhat")

# Summary: Parametrized decorators allow us to customize decorator behavior
# Instead of having fixed behavior, we can pass parameters to control how the decorator works
# This makes decorators more flexible and reusable for different scenarios


