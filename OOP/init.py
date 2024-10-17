
#Init is an special method to add attributes to class. We have to use it.
# this method take a parameter as "self" to bound with instance
class Product:
    #If we write this init like this, every created object has the same values.
    def __init__(self):
        self.name = "Samsung S24"
        print("Product instance has been created!")
    
p1 = Product()
p2 = Product()

print(p1.name,p2.name)  #Product instance has been created!
                        #Product instance has been created!
                        #Samsung S24 Samsung S24

  
class Product2:
    #If we write this init method like this, we can give this values ourselves  
    def __init__(self,name,price, isActive = False):
        self.name = name
        self.price = price
        print("Product instance has been created!")


p3 = Product2("Samsung S24",999.99)
p4 = Product2("Iphone 16",999.99,True)

print(p3.name,p3.price)
print(p4.name,p4.price)

    