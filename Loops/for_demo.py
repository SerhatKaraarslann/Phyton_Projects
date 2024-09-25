numbers = [1,5,15,35,57,72]

#1- Print each element on the list of numbers.

for x in numbers :
    print(x)

for x in reversed(numbers):
    print(x)    

#2- Which elements in that list are the multiple of 5?

for i in numbers:
    if(i % 5 == 0):
        print(i)

#3- What is the sum of the elements of list?

sum = 0

for i in numbers:
    sum += i
print("The summe of elements in list :", sum)

#4- Take the Quadrad of the elements, that is multiple of 2, in the list.

for i in numbers : 
    if(i%2 == 0):
        print(i**2)


products = ["Iphone 15","Iphone 15 Pro","Samsung S24","Samsung S24 Ultra"]

#5-Print the second character of list elements.

for i in products:
    print(i[1])

#6-How many elements, which contains "Iphone" in elements of list.

count = 0

for i in products:
    index = (i.find("Iphone"))
    if(index > -1):
        count += 1 
print(count)  
    