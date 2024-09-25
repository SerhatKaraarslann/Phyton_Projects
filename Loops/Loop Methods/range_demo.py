#1- Make an multiplicationstable

for i in range(1,11):
    print("**********************")
    for k in range(1,11):
        print(f"{i} x {k} = {i*k}")

i = 1

while (i<10):
    k = 1
    print("******************")
    while(k<10):
        print(f"{i} x {k} = {i*k}")
        k+=1
    i += 1


#2- Check a given number, if it prime or not

x = int(input("Give me a number: "))

i = 2
a = True

for i in range(2,x):
    if(x%i == 0):
        a = True
        break
    else:
        a = False

if(x == 1):
    a = False  
    
      
if(a):
    print(f"{x} is a prime number!")
else:
    print(f"{x} is not a prime!")