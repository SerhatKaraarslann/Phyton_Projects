ages = [5,12,18,24,45]

def isAdult(x):
    if x < 18:
        return False
    else :
        return True
    
# With this for loop we can filter the ages, that under 18 is.
for i in filter(isAdult,ages):
    print(i)

result = list(filter(isAdult,ages))
print(result)

#Now hier we can use lambda like that, so we dont have to use an other function
result = list(filter(lambda x : x >= 18,ages ))
print(result)

numbers = [0,1,2,6,965,34,886489,632,323245]
result  = list(filter(lambda x : x%2==0,numbers))
print(result)

names = ["Serhat","Ferhat","Julia","Uras","Havva","isa","Nora","Jaron"]
result = list(filter(lambda n : n[0].lower() == "s",names))
print(result)


result = list(map(lambda n : n.upper(),filter(lambda n: n[0].lower() == "s",names)))
print(result)

users = [
    {    "name":"Serhat Karaarslan","tweets":["tweet1","tweet2","tweet3"]},
    {    "name":"Ferhat Karaarslan","tweets":["tweet1","tweet2"]},
    {    "name":"Julia Penner","tweets":[]}
]

result = list(filter(lambda user : len(user["tweets"]) > 0,users))
print(result)

result = list(map(lambda user : user["name"].upper(),filter(lambda user : len(user["tweets"]) >0,users)))
print(result)


#with list comprehention
result = [user["name"].upper() for user in users if len(user["tweets"]) >0 ]
print(result)