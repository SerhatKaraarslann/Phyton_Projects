def greeting(name):
    return "Hello " + name


result = greeting("Serhat")
print(result)

result = greeting("Uras")
print(result)


def summe(a,b):
    return a+b

result = summe(10,20)
print(result)

def calculateAge(birthyear):
    return 2024 - birthyear

result = calculateAge(1999)
print(result)

def retirement(birthyear, name):
   age = calculateAge(birthyear)

   retire = 67 - age

   if(retire > 0):
       print(f"{name}, you have {retire} years to your retirement!")
   else:
       print(f"{name}, You are already retired! {abs(retire)} years ago.")

retirement(1994,"Serhat")
retirement(1945,"Carl")