def greeting(name):
    print("Hello ",name)

# print(greeting("Serhat"))
# print(greeting)

# We copy with  = operator not the object, we give it the adress of object
sayHello = greeting 

print(sayHello) #<function greeting at 0x000002A54FBE1440>
print(greeting) #<function greeting at 0x000002A54FBE1440>

# Same results
print(greeting('Serhat'))
print(sayHello('Serhat')) 

del sayHello # I delete sayHello not the address
# print(sayHello) #Error
print(greeting) #<function greeting at 0x0000019255B81440>


#We can declare a function in an other function
#We have to call the inner function to return the result of inner function
#otherweise the inner function is not been called.
# thats is encapsulation. the inner function has special scope itself,
#doesn't effect the outer function
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10) # 10,11

# We cant call this inner function like that, because this function has been declared in outer function
# Only outer function can be called. 
#inner_increment(10) # So error

def factorial(num):
    if not isinstance(num,int):
        raise TypeError("Number must be an integer!")
    if not num >= 0:
        raise ValueError("The number must be greater or equal to zero!")
    
    def inner_factorial(num):
        if num <= 1:
            return 1
        return num * inner_factorial(num-1)
    
    return inner_factorial(num)

try:
    print(factorial(5)) # 120

    #print(factorial(-5)) #ValueError: The number must be greater or equal to zero!

    #print(factorial("Hello")) #TypeError: Number must be an integer!

except Exception as ex:
    print(ex)
