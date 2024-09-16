#Sets in python are like list however can't be sorted and indexed.
#UNSORTED, UNINDEXED 1 element just 1 time in set

brands = {"BMW","Opel","Volkswagen","Audi","Porsche","Renault"}
brands2 = {""}

print(brands)  # each time the list is not in same sort

#result = brands[0]  #TypeError: 'set' object is not subscriptable
#print(result)

for x in brands:
    print(x)

result = "Audi" in brands
print(result)

brands.add("Skoda")

brands.update(["Lamborghini","Ferrari","Toyota"])
print(brands)

print(len(brands))

brands.remove("Opel")

brands.discard("Opellll")

brands2 = {"Citroen","Fiat"}

result = brands.union(brands2)  #to gather two sets
print(result)