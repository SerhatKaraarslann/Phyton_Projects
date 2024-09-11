# int
# float
# string
# boolean
"""
#User give the value, however the value with input is always string
x = input("x : ")
print(type(x)) #string

y = input ("y : ")
print(type(y)) #string


#With this int function the variables has been changed in integer values
x = int(input("x: "))
print(type(x))

y = int(input("y: "))
print(type(y))

"""

age = 3
weight = 1450.5
name = "Mustang"
isAuto = True

print(type(age))
print(type(weight))
print(type(name))
print(type(isAuto))

#int to float
result = float(age)

print(result)
print(type(result))


#float to int
result = int(weight)

print(result)
print(type(result))

# bool to str
result = str(isAuto)

print(result)
print(type(result)) #"True"

#bool to int
result = int(isAuto)

print(result)         #1  True == 1
print(type(result)) 