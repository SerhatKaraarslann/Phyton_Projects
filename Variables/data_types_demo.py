"""
Circle area : PI.R.R
Circle around : 2.PI.R
Pi = 3.14
"""

pi = 3.14
radius = float(input("Enter the radius of circle : "))

print("The radius of circle : ",radius)

area = float(pi*radius**2)

print("The area of circle : ",area)

"""
In this example will be calculate the road long of an auto in mile,
which given in km
mile = km/1.609344
"""

road = float(input("Please enter the road long of auto in km : "))
print("The road long in km : ",road)

mile = round(road/1.609344,2) 

print("The auto has been driven ", mile, " miles!")