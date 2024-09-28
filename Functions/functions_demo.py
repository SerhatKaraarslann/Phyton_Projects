#1- Write a function, which prints the given name to the screen at the given times.

def printName(name,number):
    for x in range(number):
        print(name)

printName("Serhat",5)

#2- Write a function, that calculates the area and perimeter of a rectangle.



def calculateArea():
    side = int(input("Please give the side lengt of rectangle : "))
    side1 = int(input("Please give the side lengt of rectangle : "))
    return f"The area of rectangle : {side*side1}"

result = calculateArea()
print(result)

def calArea(side1,side2):
     return f"The area of rectangle : {side1*side2}"

result = calArea(6,7)
print(result)

def calculatePerimeter():
    side = int(input("Please give the side lengt of rectangle : "))
    side1 = int(input("Please give the side lengt of rectangle : "))
    return f"The perimeter of rectangle : {(side+side1)*2}"

result = calculatePerimeter()
print(result)

def calPer(side1,side2):
     return f"The perimeter of rectangle : {2*(side1+side2)}"

result = calPer(6,7)
print(result)

#3- make coin toss application with random module

def coinToss():
    import random
    number = random.random()

    if number > 0.5:
        return "Heads"
    else:
        return "Tails"
    
print(coinToss())
#4- write a function, which find all of prime numbers between the given two numbers

def findPrime(start, end):
    primes = []
    for number in range(start,end+1):
        if(number > 1):
            for i in range(2,number):
                if(number % i == 0):
                    break
            else:
                primes.append(number)
    return primes

result = findPrime(2,10)
print(result)

#5- Write a funciton, which finds all of divisors of a given number.

def findDivisors(number):
    dividors = []
    for i in range(1,number+1):
        if(number % i == 0):
            dividors.append(i)
    return dividors

result = findDivisors(45)
print(result)