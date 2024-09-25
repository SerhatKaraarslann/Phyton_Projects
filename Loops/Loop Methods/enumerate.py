brands = ["Opel","Audi","BMW","Mercedes","Volkswagen"]

index = 0
for brand in brands:
    index +=1
    print(f"{index} - {brand}") #1-Opel 2-Audi ....


#enumerate

obj1 = enumerate(brands)

print(type(obj1)) #enumerate
print(list(obj1)) #[(0,"Opel"),(1,"Audi"),...]

for index,value in enumerate(brands,10):
    print(index,value) #10 Opel 11 Audi ...


#zip

list1 = [1,2,3,4,5,6]
list2 = ["a","b","c","d","e"]

list3 = list(zip(list1,list2))

print(list3)

list4 = [100,200,300,400,500,600]

list5 = list(zip(list1,list2,list4))
print(list5)


for item in zip(list1,list2):
    print(item)

for a,b,c in zip(list1,list2,list4):
    print(a,b,c)