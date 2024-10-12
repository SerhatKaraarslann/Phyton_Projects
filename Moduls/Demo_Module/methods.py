import db 

def addProduct(name,price):
    db.products.append(
        {
            "id":len(db.products) + 1,
            "name" : name,
            "price" : price
        }
    )

def updateProduct(id,name,price):
    for product in db.products:
        if(product["id"] == id):
            product["name"] = name
            product["price"] = price
            break


def getProducts():
    for product in db.products:
        print(f"id : {product["id"]} product name : {product["name"]} price : {product["price"]}")