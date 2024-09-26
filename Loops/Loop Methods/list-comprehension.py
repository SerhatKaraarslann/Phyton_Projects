numbers = []

for i in range(10):
    numbers.append(i)

print(numbers)   #[0,1,2,3,4,5,6,7,8,9]


#[ expression for item in list]
numbers2 =[x for x in range(10)]

print(numbers2)    # [0,1,2,3,4,5,6,7,8,9]

numbers3 = [x*2 for x in range(5)] # [0,2,4,6,8]
print(numbers3)

name = "Serhat Karaarslan"

result = [c.upper() for c in name]
print(result)


names = ["Hüseyin","Emine","Serhat","Uras"]

result =[name.lower() for name in names]

print(result)