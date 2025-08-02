def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

# We can give a function as a parameter to other function
def operation(f1,f2,f3,f4, op_name):
    if op_name == "add":
        print(f1(2,3))
    elif op_name == "sub":
        print(f2(5,3))
    elif op_name == "mult":
        print(f3(3,4))
    elif op_name == "div":
        print(f4(18,3))
    else:
        print("Invalid operation!")


operation(add,sub,mult,div,"add") # 5
operation(add,sub,mult,div,"sub") # 2
operation(add,sub,mult,div,"mult") # 12
operation(add,sub,mult,div,"div") # 6.0
operation(add,sub,mult,div,"aaaadd") # Invalid operation