x = 10

# If we want to raising an exception we re using this word, raise than the exception

if(x > 5):
    raise ValueError("X can not be greater than 5!")

def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(text) is not str:
        raise TypeError("color have to be str typ!")

    if type(color) is not str:
        raise TypeError("color have to be str typ!")
    
    if color not in colors:
        raise ValueError("Undefined color name!")
    
    print(f"{text} {color} has been written!")
    
try:
    colorize("Hello",10)
    colorize("Hi","blue")
except Exception as ex:
    print(ex)