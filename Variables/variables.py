#We buy a product that costs 5000 Euros.
# and wanna add tax (%19).

print("Product costs : " ,5000+5000*(19/100))

#We have to write this for each products
#instead of this, we use variables

productX = 5000
productY = 11000
tax = 0.19

print("Product costs : ",productX+productX*tax)
print("Product costs : ",productY+productY*tax)

#Now we can change easily tax or product cost in variables
#then our product cost has been changed.

print("Product costs : ",productX+productX*tax)

tax = 0.2
print("Product costs : ",productX+productX*tax)

#we can define and print variables in one line
a,b,c = 10,20,30.7
print(a,b,c)

name = "Serhat"
name = 'Serhat'

print(type(name))


isStudent = True
print(type(isStudent))

x,y,z = 11.9, "Serhat", False
