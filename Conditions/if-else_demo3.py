#1- Make a python application that checks the user's ability to get a driver's license by asking for name, age and education information.
#** The minimum age to get a driver's license must be 18 and education must be high school or university.

name = input("name and surname : ")
age = int(input("Age : "))
education = input("Education : ")

if(age >= 18):
    if(education == "highschool" or education == "univercity"):
        print("You can have a driver licence!")
    else:
        print("Your education is not okay to have a driver licence!")
else:
    print("You are under 18, you can not have a driver licence!")

#2- Make a python application that takes a student's 2 written and one oral grades and prints the grade information corresponding to the grade range according to the calculated average.

visa1 = int(input("Visa1 : "))
visa2 = int(input("Visa2 : "))
final = int(input("Final : "))

result = (visa1 + visa2+ final)/3

if(final < 50):
    print("Your final note is under 50, you can not pass the exam!")
else:
    if(0 <= result <= 24 ):
        print(f"Your note is {result} F! You failed!")
    elif(25<= result <= 44):
        print(f"Your note is {result} F! You failed!")
    elif(45 <= result <= 54 ):
        print(f"Your note is {result} D! You pass!")
    elif(55 <= result <= 69 ):
        print(f"Your note is {result} C! You pass!")
    elif(70 <= result <= 84 ):
        print(f"Your note is {result} B! You pass!")
    elif(85 <= result <= 100 ):
        print(f"Your note is  {result} A! You pass!")
      


"""3- Make a python application that calculates the service time of a vehicle with a traffic release date according to the following information.

#1. Maintenance => 1st year

2nd Maintenance => 2nd year

3rd Maintenance => 3rd year

** Calculate the duration based on the day, month, year information received."""

import datetime

dateToTrafic = input("When was your vehicle on the road first time : ")
dateToTrafic = dateToTrafic.split('/')


now = datetime.datetime.now()
traficTime = datetime.datetime(int(dateToTrafic[0]),int(dateToTrafic[1]),int(dateToTrafic[2]))

distanceTime = now - traficTime
day = distanceTime.days

print(day)

if(day <= 365):
    print("1.service maintanence")
elif(365<day and day <= 365*2):
    print("2. service maintanence")
elif(day>365*2 and day <= 365*3):
    print("3.service maintanence")
else:
    print("Wrong info!")


