msg = "Welcome to our Python Course. Do you love Python?"

# List is the array in the other program language

msg = msg.split()

print(msg[0][0])
print(msg)

numbers = [1,3,5,7,9]

print(numbers)

print(numbers[4])
# print(numbers[7]) #IndexError : list index out of range

print(type(numbers[0]))

names = ["Ahmet","Serhat","Uras","Julia","Nora","Jaron"]

print(type(names[0]))

list = ["Serhat",29, "Julia",27]  # We can write in a list different types of variables
list2 = ["Jaron",4,"Nora",2]

list3 = [["Julia",27],["Nora",2]]
list4 = [list,list2]
