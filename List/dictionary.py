# A dictionary is a collection which is UNORDERED, CHANGEABLE and INDEXED.
# We can use sort method in Dictionary.
# Dictionaries are written with curly brackets and they have keys and values.

#thisdict = {"brand" : "Ford","model" : "Mustang","year":1969}

cities = {
    "Istanbul" : 34,
    "Izmir" : 35,
    "Manisa" : 45,
    "Aydin" : 9,
    "Ankara" : 6
}

result = cities["Ankara"]   #6
print(result)

cities["rize"] = 53   #changeable
print(cities)

students = {      # we can write a dictionary in a dictionary.
    100:{
    "name" : "Serhat",
    "surname" : "Karaarslan",
    "age":29,
    "notes" : [90,95,93]
        },
    101:{
    "name" : "Ferhat",
     "surname" : "Karaarslan",
    "occupy" : "Tecniker"
        },
    102:{
        "name" : "Julia",
        "surname" : "Penner",
        "age" : 26,
        "occupy" : "Sozialarbeiterin"
    }

        }

print(students[100])
print("\n")
print(students)

print (students[100]["name"])  #Serhat
print(students[100]["notes"][1])  #95