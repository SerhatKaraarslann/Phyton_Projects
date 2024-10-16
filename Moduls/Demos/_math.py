import math

value = dir(math)   # wih this dir method i copy all methods in math module to value 
#print(value)

#value = help(math) # if want to see more information about methods, i should use this method
#print(value)

#value = help(math.factorial) # to see information about the factorial method
#print(value)

result = math.sqrt(49)
print(result)

result = math.factorial(6)
print(result)

result = math.floor(6.7)
print(result)

result = math.ceil(7.3)
print(result)



# if I import or define a method with the same name other
# it will be used this function, if this method under the import
#however if the method has been defined before import, it will be used the import method 
from math import factorial,sqrt,ceil

def sqrt(x):
    print("x : "+ str(x))

result =sqrt(49)
print(result)