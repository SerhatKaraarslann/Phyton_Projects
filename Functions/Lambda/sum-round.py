numbers = [32,4,67,345,897,34,54]

result = sum(numbers,10)  # 1433(from numbers) + 10

print(result)

products = [
    {"title" : "Iphone 15","price" : 799.99},
    {"title" : "Iphone 15 Max","price" : 899.99},
    {"title" : "Iphone 16","price" : 999.99},
    {"title" : "Iphone 16 Max","price" : 1099.99},
    {"title" : "Samsung S24","price" : 799.99},
    {"title" : "Samsung S25","price" : 0}
]

sumPrice = sum([product["price"] for product in products])
productNum = len([product for product in products if product["price"] > 0])

result = sumPrice/productNum

print(result)


result = round(10.2)   # 10
print(result)

result = round(10.6)   #11
print(result)

result = round(10.5)    #10
print(result)

result = round(1.4262422,2)   #1,43
print(result)     

result = round(1.4262422,4)   #1,4262
print(result)           