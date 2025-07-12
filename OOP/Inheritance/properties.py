# In python thera are no private or public keywords, which descripes a method or an instance parameter.
class Product:
    def __init__(self,name, price, description):
        self.name = name
        self.description = description
        if(price  >= 0):
            self._price = price
        else:
            raise ValueError("Price can not have a negative value!")

# we want to change the price but we shouldn't use direkt initialize here. We have to use a method for it.
# Its the same to get price.
#Or alternatively we can use properties.    

    # def set_price(self,value):
    #     if(value  >= 0):
    #         self._price = value
    #     else:
    #         raise ValueError("Price can not have a negative value!")
        

    # def get_price(self):
    #     return self._price
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price can not have a negative value!")
        

    @property
    def short_description(self):
        return self.description[:10]

p = Product("Iphone 15",899, "Iphone 15 has been created from Apple.")

print(p.name)

#print(p.get_price())

#p._price = 566 # we dont use this now 
#p.set_price(-600) 
#print(p._price) 

print(p.price) # we call as a property not like a method.

#p.price = -900

#print(p.price)

print(p.short_description)


#The @property decorator in Python is used to turn a method into a read-only attribute. It allows you to define a method that can be accessed like an attribute, without needing to call it with parentheses.
#It’s useful when:

   # You want to control access to an attribute.
   # You want to compute a value dynamically but still access it like a regular variable.
   # You want to hide internal implementation details from the user of your class.

class Circle:
    def __init__(self, radius):
        self._radius = radius


    @property
    def area(self):
        return 3.14159 * self._radius ** 2


    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value



c = Circle(5)
print(c.area) # No parentheses needed!
