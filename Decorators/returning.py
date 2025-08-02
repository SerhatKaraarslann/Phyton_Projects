# Our function kann return a function as a value
def power(number):

    def inner(pow):
        return number ** pow
    
    return inner

two = power(2)
print(two(3)) # 8

three = power(3)
print(three(4)) # 81

def ask_permission(page):
    def inner(role):
        if role == 'Admin':
            return "{} can reach at {}.".format(role,page)
        else:
            return  "{} can't reach at {}.".format(role,page)
        
    return inner
        
user1 = ask_permission("Product Edit")
print(user1('Admin'))

user2 = ask_permission("Product Edit")
print(user2('User'))


def operation(operator_name):
    def add(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    
    def mult(*args):
        mul = 1
        for i in args:
            mul *= i
        return mul
    
    if operator_name == "add":
        return add
    else:
        return mult
    

operation1 = operation("add")
print(operation1(4,5,6,7,8)) # 30

operation2 = operation("mult")
print(operation2(4,5,6,7,8)) #6720