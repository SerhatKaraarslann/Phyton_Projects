# All Function returns True, if all elements of list are True 

result = all([True, True, False])
print(result)    #false 

result = all([True,True,True])
print(result)   #True


result = all({True,False,True})
print(result)     #False

# If just an element True in the list, with ANY function is been returned True.

result = any({True, False, False})
print(result)       #True


#And => True and True => True => All()
#Or => True or False => True => Any()


numbers = [0,1,3,5,6,8,9,10]
result = all([bool(number) for number in numbers])

print(result)    #False cause of 0 = False

result = any([bool(number) for number in numbers])
print(result)   #True

result = all([bool(number) for number in numbers if number%2 == 1])
print(result)   #True

result = all([number%2 == 0 for number in numbers])
print(result)    #False = [True,FAlse,False,False,True, True, False, True]

result = any([number%2 == 0 for number in numbers])
print(result)    #True = [True,FAlse,False,False,True, True, False, True]

persons = ["Serhat","Ferhat","Carlos","Julia","Nora","isa","jaron","havva","Uras"]
result = all([person[0].lower() == "s" for person in persons])
print(result)   #False  => [True, False, False, False, False, False, False, False, False]

result = any([person[0].lower() == "s" for person in persons])
print(result)   #True  => [True, False, False, False, False, False, False, False, False]