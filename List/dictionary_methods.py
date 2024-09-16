carObj = {
    "brand" : "BMW",
    "model" : "M3",
    "year"  : 2023
}

result = carObj["brand"]  #result = carObj.get("brand") same
print(result)

result = carObj.get("brand")  #BMW
print(result)

for x in carObj:   #key
    print(x)

for x in carObj:    #value
    print(carObj[x])

for x in carObj:                        #for x,y in carObj.items():
    print(f"{x} :  {carObj[x]}")                #  print(x,y)

for x in carObj.values():  #to take values
    print(x)

for x,y in carObj.items():
    print(x,y)

result = "branddd" in carObj
print(result)

result = len(carObj)
print(result)

carObj["color"] = "dark blue"
print(carObj)

carObj.pop("color")
print(carObj)

#carObj.popitem()  #delete the last item

#del carObj["brand"]
#print(carObj)

#del carObj
#print(carObj)

#carObj.clear()  # to clear dictionary
#print(carObj)

print(carObj)
obj = carObj  # reference copy, adress copy
obj["brand"] = "Mazda" 
print(obj)

obj = carObj.copy()  # to copy(not reference) in other dictionary
print(obj)

carObj.update({"brand" : "BMW",
               "color" :"darkblue"})

print(carObj)