# This is a basic decorator that logs function information
# Problem: When we use this decorator, the decorated function loses its original metadata
# The function's __name__ and __doc__ will be replaced with the wrapper's metadata

def log_data(fn):
    def wrapper(*args,**kwargs):
        """
        Information about wrapper
        """
        print(f"The called method name : {fn.__name__}")
        print(f"Method infos: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper

@log_data
def add(x,y):
    """
    This function adds the two parameters.
    """
    return x + y

# Let's test the function and see what happens to its metadata
print(add(10,20))
print(add.__name__) #wrapper - This shows "wrapper" instead of "add"!
print(add.__doc__)  #None - This shows wrapper's docstring instead of add's docstring!

# Solution: Use functools.wraps to preserve original function metadata
# @wraps(fn) copies the original function's metadata to the wrapper function
# This solves the problem of losing function name and docstring

from functools import wraps

def log_data2(fn):
    @wraps(fn)  # This line preserves the original function's metadata!
    def wrapper(*args,**kwargs):
        """
        Information about wrapper
        """
        print(f"The called method name : {fn.__name__}")
        print(f"Method infos: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper


@log_data2
def add2(x,y):
    """
    This function adds the two parameters.
    """
    return x + y

# Now let's test the improved decorator with @wraps
# The metadata should be preserved correctly this time
print(add2(10,20))
print(add2.__name__)  # This will show "add2" - correct!
print(add2.__doc__)   # This will show the original docstring - correct!