name = "Serhat"
surname = "Karaarslan"
age = 29

print("My name ist {} {}".format(name,surname))

print("My name is {1} {0}".format(name,surname)) #My name is Karaarslan Serhat

print("My name is {s} {n}".format(n = name,s=surname))

print("My name is {} {}. I'm {} years old.".format( name,surname,age))

result = 200/700

print("The rsult is {n:1.3}".format(n=result))

print("The result is {}".format(round(result,3)))

print(f"My name is {name} {surname} and I'm {age} years old.")