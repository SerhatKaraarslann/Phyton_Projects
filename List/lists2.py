languages = ["Python","Java","Javascript","C"]

result = languages

print(result)

print(type(result))  #list

result = languages[0:2]  # Python ,Java
result = languages[-1]   #C
result = languages[-3:]  #Java, javascript, C
result = languages[2:]   #Javascript ,C

print(result)


languages[-1] = "HTML"

print(languages)  # Python, java, javascript,Html

result = len(languages)  #4

print(result)

result = languages + ["Go","C#"]
print(result)

print(languages)  # languages has not changed but result, yep

if "Python" in languages:
    print("True")


for x in languages:
    print(x)


del languages[0]   # to erase any object in list with index number
print(languages)