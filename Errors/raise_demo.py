#1- Create a factorial function and give error messages for the incoming value to the function.

def fact(x):
    x = int(x)

    if( x < 0):
        raise ValueError("X can't be negativ!")
    result = 1
    for i in range(1,x+1):
        result *= i
    
    return result

for i in [5,7,2,-4,"10a"]:
    try:
        x = fact(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)
        

#2- Give an German character error for the entered password value.

def passControl(password):
    german_Characters = "üöäß"

    for i in password:
        if i in german_Characters:
            raise TypeError("Password can not involve a german character!")
        
    print("Access granted!!!")

password = input("password : ")

try:
    passControl(password)
except TypeError as e:
    print(e)

