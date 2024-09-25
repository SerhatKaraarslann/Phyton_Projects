products = [
    {"name":"Iphone 13","price":"399.99"},
    {"name":"Iphone 13 Pro","price":"499.99"},
    {"name":"Iphone 14","price":"599.99"},
    {"name":"Iphone 15","price":"799.99"},
    {"name":"Iphone 15 Pro","price":"899.99"},
    {"name":"Samsung S24 Ultra","price":"999.99"},
]


#1-List all products informationen.

for info in products:
    print(info)

#2-What is the sum price of all products?

priceSum = 0

for product in products:
   priceSum += float(product["price"])
print(priceSum)

#3-Show the products, which prices more than 500.

for product in products:
    if(float(product["price"]) > 500):
        print(product)

#4-Find the products with an key, which given by user.

key = input("Please give the model of phone :")

for product in products:
    if(product["name"].find(key) > -1):
        print(product)