#for item in list:
#    if(condition):
#        expression

numbers = [1,5,8,9,15,44]

result = []

for number in numbers:
    if(number% 2 == 0):
        result.append(number)

print(result)


#[expresiion for item in list if condition]

result = [number for number in numbers if(number%2 == 0)]    #[8,44]
print(result)    


result = [number if(number%2 == 0) else "Even" for number in numbers] #["Even","Even",8,"Even","Even",44]
print(result)




#with for loop
prices = [100,200,500,0,400]

taxes = []

for price in prices:
    if(price > 0):
        taxes.append(price*1.18)

print(taxes)


#with list comprehension

taxes = [price*1.18 for price in prices if(price>0) ]

print(taxes)


taxes1 = [price*1.18  if(price) else "Tax hasnt been calculated"for price in prices]

print(taxes1)


#without list comprehension
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

#with list comprehension

result1 = [(x,y) for x in range(3) for y in range(3)]
print(result1)


result2 = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(result2)