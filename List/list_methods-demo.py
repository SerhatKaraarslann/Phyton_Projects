names = ["Isa","Serhat","Ferhat","Uras","Havva","Julia","Nora","Jaron"]
ages = [1963,1994,1990,2022,1969,1997,2022,2020]

#1-Add "Nina" the end of the names

names.append("Nina")
print(names)

#2- Add "Seda" the first on the list

names.insert(0,"Seda")
print(names)

#3-Delete "Nora" from the list

names.remove("Nora")
print(names)

#4-what is the index of "Julia"?

result = names.index("Julia")
print(result)

#5- Is "Carlos" an element of list?

result = names.count("Carlos")
print(result)

result = "Carlos" in names
print(result)

#6-reverse the elements of list

names.reverse()
result = names
print(result)

#7-Sort the elements of list alphabetic

names.sort()
result = names
print(result)

#8- sort the list of ages chronologic

ages.sort()
result = ages
print(result)

#9-Make a list from str = "Iphone X,Iphone XR" 

str ="Iphone X, Iphone XR"
result = str.split(",")
print(result)

#10-wihch is the biggest element in ages.

result = max(ages)
print(result)

#11-How many 2022 in the ageslist?

result = ages.count(2022)
print(result)

#12- delete the all elements of ageslist

ages.clear()
print(ages)

#13- make a list with element, that you have from user

brands = []
brand = input("brand : ")
brands.append(brand)
brand = input("brand : ")
brands.append(brand)
brand = input("brand : ")
brands.append(brand)

print(brands)