numbers = [1,2,5,7,9]

numberExp = []

for i in numbers:
    numberExp.append(i**2)

print(numberExp)  #[1,4,25,49,81]


# if we want to make some difference with all of elements of list 
# and have them as a list, we can use map function

def square(number):
    return number **2

result = list(map(square, numbers))

print(result)

#we can use here lambda function too

result = list(map(lambda a : a**2,numbers ))
print(result)


#with list comprehension

result = list(x**2 for x in numbers)

print(result)

#Str to int
numbersStr =["1","2","5","7","9"] 

result = list(map(int,numbersStr))
print(result)

#################################
names = ["serhat","ferhat","havva","isa"]

result = list(map(len,names))
print(result)

result = list(map(str.capitalize,names))
print(result)

result = list(map(str.upper,names))
print(result)


#####################################
users = [
    {"name":"Serhat","surname": "Karaarslan"},
    {"name" :"Julia","surname":"Penner"}
    ]

result = list(map(lambda x: x["name"],users))
print(result)