import random

result = dir(random)
#print(result)

#result = help(random)

result  = random.random() #0.0 - 1.0
print(result)

result = random.random()*100 
print(result)

result = random.uniform(1,10) # with this method we can take a random float number between the given two parameters
print(result)

result = int(random.uniform(10,100))
print(result)

result = random.randint(10,100) # to take a int number between two parameters
print(result)

names = ["Serhat","Ferhat","Ali","Isa","Uras","Havva","Seda"]
result = names[random.randint(0,len(names)-1)]
print(result)

result = random.choice(names) # this method choice a random element from a list
print(result)

greeting = "Hello"
result = random.choice(greeting)
print(result)


list1 = list(range(10)) #that makes a list from 0 to 9
print(list1)

random.shuffle(list1)  # to make a list shuffled
print(list1)

list2 = range(100)

result = random.sample(list2,3) # the method, that take a 3 random element from list2
print(result)

result = random.sample(names,2)
print(result)