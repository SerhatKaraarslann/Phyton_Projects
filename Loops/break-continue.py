numbers = [1,2,3,4,5,6,8,9]
name = "Serhat Karaarslan"

for letter in name :
    if(letter == "h"):
        continue       #Serat Karaarslan
    print(letter)


for letter in name:
    if(letter == "h"):
        break           #Ser
    print(letter) 


i = 0
while i < 5:
    if(i == 4):
        break
    print(i)
    i+=1

print("Loop has been ended!")


#The sum of the numbers between  1-100

i = 0
sum = 0
while ( i<= 100):
    i+=1
    if(i%2 == 1):
        continue
    sum +=i
    

print(f"Sum : {sum}")