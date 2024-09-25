"""
Keep the unlimited product information you will receive from the user in the products list.

   ** ask the user for the number of products.

   ** Let the dictionary list structure be (name, price).

   ** When the product addition process is finished, list the products on the screen with while
"""


products = []

piece = int(input("How many products do you want to add? : "))

i = 0

while(i < piece):
    productname = input("Product name : ")
    price = input("Price : ")
    products.append({
        "name" : productname,
        "price": price
    })
    i+=1

for product in products:
    print(product)