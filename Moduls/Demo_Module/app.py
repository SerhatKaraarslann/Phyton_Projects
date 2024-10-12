"""
module1 (db)       : products
module2 (methods)  : addProduct(),updateProduct(), getProducts()
module3 (app)      : 

                    add new Product => addProdcut("Iphone 14 Pro",899.99)
                    update Prodcut  => updateProdcut("Iphone 15 Pro",999.99)
                    list products   => getProducts()
"""

from methods import *

getProducts()
print("*************************")

addProduct("Iphone 16 Max",1099.99)
getProducts()
print("*************************")

updateProduct(8,"Iphone 16 Ultra",1299.99)
getProducts()