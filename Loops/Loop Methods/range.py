#list1 = [3,5,7,9]

#for i in list1:
#    print(i)

r = range(10)  # with this method we can create a list

result = list(r) 

print(result)  #[0,1,2,3,4,5,6,7,8,9]

r2 = range(2,5)  # we can give a start and stop however start is inside stop outside

result = list(r2)

print(result)  # [2,3,4]


r3 = range(50,100,10) #we can start stop and step too.

result = list(r3)
print(result)     # [50,60,70,80,90]

r4 = range(100,50,-10)
result = list(r4)
print(result)       #[100,90,80,70,60]



for i in range(10):
    print(i)    # 0,1,2,3,4,5,6,7,8,9

for i in range(5,10):
    print(i)     # 5,6,7,8,9

for i in range(100,200):
    if(i%2 == 0):
        print(i)