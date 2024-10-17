#Class
# We create a class with class keyword then ":". In class we have methods and atrributes 
class Student:   
    #method
    #attribute
    pass


#To create an object(instance) from this class, first "object_name = Classname()"
#Object,Instance

student = Student()

print(type(student))  #<class '__main__.Student'>
print(student)        #<__main__.Student object at 0x00000229F8FD9B80>

student2 = Student()
print(student2)       #<__main__.Student object at 0x000002A5C2059BB0>

class Product:
    pass

product = Product() #Samsung 24
product2 = Product() #Iphone 16
product3 = Product()  # Iphone 16 Max

products = [product,product2,product3]

for product in products:
    print(product)
    print(type(product))