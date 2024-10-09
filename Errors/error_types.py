x = int(input("x: "))
y = int(input("y : "))

#print(x/y) 
# # x = 10, y = 0 ZeroDivisionError: division by zero
# x = 10, y = 20a ValueError: invalid literal for int() with base 10: '20a'

#Error Types
#1-Syntax Error

#hlklkdlk;;

#def write(():
#    pass

#print("Hell"o)

#2-Name Error => undefined variable using

#print(name)

#3-Type Error => using false parameter

#len(5) #TypeError: object of type 'int' has no len()
#4 + "a" #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#4-Index Error => List, Tupel , Set or Dictionary or String have no element with that indexnumber

list1 = ["Hello"]
# list1[1] #IndexError: list index out of range

#5-Value Error => using a false typ 

#int("10a")  #ValueError: invalid literal for int() with base 10: '10a'

#6-KeyError => Like index error although specific for dictionary

d = {}
#d["name"] #KeyError: 'name'

#7-Attribute Error => Using no attribute

"hello".upper() #normal
"hello".Upper() #AttributeError: 'str' object has no attribute 'Upper'. Did you mean: 'upper'?

#8- There are a lot error types like Memory Error,NotImpelementedError, OS Error ...