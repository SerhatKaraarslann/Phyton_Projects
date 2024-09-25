numbers  = [1,2,3,4,5,6,7,8,9,0]

#print(numbers[0])
#print(numbers[1])
#print(numbers[2])
#print(numbers[3])

for x in numbers:
    print(x)

for i in numbers:
    print("Hallo")


names = {"Serhat","Ferhat","Julia","Isa Uras"}

for name in names:
    print(name)

name = "Serhat Karaarslan"

for a in name:
    print(a)

tuple1 = [(1,2),(2,3),(4,5),(6,7)]

for a in tuple1:  #(1,2),(2,3),(4,5),(6,7)
    print(a)

for a,b in tuple1: # 1 2 2 3 4 5 6 7
    print(a,b)

dict1 = {"ST":"Steinfurt","MS":"Münster","OS":"Osnabrück","K":"Köln"}

for x in dict1:  #ST,MS,OS,K
    print(x)

for x in dict1.values(): # Steinfurt, Münster, Osnabrück, Köln
    print(x)

for key, value in dict1.items():  
    print(key,value)