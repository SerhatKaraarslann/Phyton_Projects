import module  
# If i want to methods or something in other module, i have to import it in the using class.
#import module-name


# if i want to call a variable or method first the module_name, that has been imported, than (.) the variable or method name
result = module.number
print(result)

result = module.numbers
print(result)

result = module.summe(50,60)
print(result)

result = module.students["name"]
print(result)

result = module.students["notes"]
print(result)


#we can import module like this as a give a name
import module as m

result = m.number
print(result)

# if we want to import just a part of module
from module import students,summe

result = students
print(result)

result = summe(30,40)
print(result)

#if i want to import all of them from module and now i dont need to use module name, with their name on the module i can call them
from module import *

result = students
print(result)