"""
Try to find a randomly generated number between 1-100 with more or less expressions

   ** Search “python random” for “random module”.

   ** Score out of 100. Each question is worth 20 points.

   ** Take the rights information from the user and calculate each question based on the number of lives specified.
"""
import random

number = random.randint(1,10)

live = int(input("How many live do you wanna have? : "))
count = 0



while(live > 0):
        live -= 1
        count += 1
        prediction = int(input("Give me your prediction : "))                
        if(number > prediction):
                print("The number is greater than your prediction!")
                
        elif(number < prediction):
                print("The number is less than your prediction!")
                
        else:
                score = 100 - (count-1)*(100/live)
                print(f"Your live : {live} and your score : {score}")
                break


    