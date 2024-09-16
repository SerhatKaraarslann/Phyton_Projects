#1- Take 3 productsinfo from user and pack them in dictionary

id1 = int(input("id : "))
name1 = input("name : ")
price1 = float(input("price : "))

id2 = int(input("id : "))
name2 = input("name : ")
price2 = float(input("price : "))

id3 = int(input("id : "))
name3 = input("name : ")
price3 = float(input("price : "))

products = {id1 : {
    "name" : name1,
    "price" : price1
},
id2:{
    "name" : name2,
    "price" : price2
},
id3 : 
{
    "name" : name3,
    "price" : price3
}}

print(products)

#2- Take product id from users and show the productinfos.

id = int(input("Please give us an id number : "))

product = products[id]

print(f'id: {id} product name : {product["name"]} price : {product["price"]}')