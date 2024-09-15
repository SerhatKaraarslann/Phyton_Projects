# 1 - Create a list with variables "Samsung S22, Samsung S23, Samsung S24, Samsung S24 5G"

phones = ["Samsung S22","Samsung S23","Samsung S24","Samsung S24 5G"]
print(phones)

#2- How many elements has the list?

result = len(phones)
print(result)

#3-The first and the last elements of list?

first = phones[0]
print("First element on the list :",first)

last = phones[-1]
print("The last element on the list : ",last)

#4-Change the variable "Samsung S22" to "Samsung S22 5G"

phones[0] = "Samsung S22 5G"
print(phones)

#5-Is "Samsung S23" an element of list?

if "Samsung S23" in phones:
    print("Yes")

#6- Which element is the -3. element on the list?

x = phones[-3]
print(x)

#7- Print the first 2 elements of list.

result = phones[0:2]
print(result)

#8- Add "Samsung Note 4" and "Iphone 15 Plus" on the list instead of the last 2 elements.

phones[-1] = "Samsung Note 4"
phones[-2] = "Iphone 15 Plus"

print(phones)

#9-Add the list "Iphone 15" and "Iphone 16 Max"

result = phones + ["Iphone 15","Iphone 16 Max"]
print(result)

#10- delete the last element of list

del result[-1]
print(result)

#11-print reverse the elements of list

result = phones[::-1]
print(result)

#12- print the list elements

for a in phones:
    print(a)