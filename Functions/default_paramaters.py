def greeting(name,text):
    print( f"{text} {name}")

greeting("Serhat","Welcome home")
greeting("Julia","Where have you been")

def greeting2(name, text = "Have a nice day"):  # We can define the parameter like this.
    print(f"{text} {name}")
 
greeting2("Serhat")  # Now, we dont meet a problem/error, with giving just the another parameter
greeting2("Uras","How are you") # we can define extra 


def exponent(basis,exp = 3):
    return basis**exp

result = exponent(2)
print(result)

#def exponent2(basis = 3,expo): # Non-default argument follows default argument


def summe (a,b):
    return a+b

def sub(a,b):
    return a-b

def calculation(a,b,fn):   # A function can be used in other function as a parameter or a part
    return fn(a,b)

result = calculation(4,5,summe)
print(result)

result = calculation(4,5,sub)
print(result)