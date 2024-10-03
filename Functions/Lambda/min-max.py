#With this two functions we can find the minimum or maximum element of a list.
#as alphabetic or as decimal

numbers = [1,5,7,45,25,89,23,1223]
letters = ["a","d","x","t","r","j"]

result = min(numbers)
print(result)           #1
print("###########################################")

result = max(numbers)
print(result)           #1223
print("###########################################")

result = min(letters)
print(result)           #a
print("###########################################")

result = max(letters)
print(result)           #x
print("###########################################")

names = ["Serhat","Julia","Uras","Isa","Nora","Idil"]

result = min(names)
print(result)           #Idil
print("###########################################")

result = max(names)
print(result)           #Uras
print("###########################################")

result = min(len(name) for name in names)
print(result)           #3
print("###########################################")

result = max(len(name) for name in names)
print(result)           #6
print("###########################################")

result = max(names, key = lambda n : len(n))
print(result)           #Serhat
print("###########################################")

result = min(names,key = lambda n:len(n))
print(result)           #isa
print("###########################################")

products = [
    {"title" : "Iphone 15","price" : 799.99},
    {"title" : "Iphone 15 Max","price" : 899.99},
    {"title" : "Iphone 16","price" : 999.99},
    {"title" : "Iphone 16 Max","price" : 1099.99},
    {"title" : "Samsung S24","price" : 799.99}
]

result = min(products,key = lambda n : n["price"]) #{'title': 'Iphone 15', 'price': 799.99}
print(result)

result = max(products,key = lambda n : n["price"])["title"] #Iphone 16 Max
print(result)

