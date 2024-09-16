#Tuples are like list however unchangeable. We can use some methods on tuples.
#We can add or remove new elements
#UNCHANGEABLE!!!

list1 = [1,2,3]
tuple1 = (1,2,3)  # tuple1 = 1,2,3 .We can use "()" or not. Doesnt matter.

print(type(list1))
print(type(tuple1))


tuple2 = (1,"iki",True)
print(tuple2[2])

print(len(tuple1))
print(len(list1))

list1[1] = 5
print(list1)

#tuple1[1] = 5   #TypeError: 'tuple' object does not support item assignment
#print(tuple1)

list1.append(11)
print(list1)

#tuple1.append(11)   #AttributeError: 'tuple' object has no attribute 'append'
#print(tuple1)

print(tuple1.count(1))
print(tuple1+tuple2)  #we can write so but this doesnt change tuples

tuple3 = tuple([3,4,5,6,7])  #to make tupel from a list
print(tuple3)