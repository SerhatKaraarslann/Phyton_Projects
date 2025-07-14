class MyDictionary(dict):
    def __repr__(self):
        print("You have a message from repr method.")
        return super().__repr__()
    
    def __missing__(self,key):
        print(f"You called a key value '{key}' which doesn't exist!")
        return None  # Return None for missing keys

    
    def __getitem__(self,key):
        print("You call an element.")
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)
    
    def __setitem__(self,key,value):
        print("You add an element in the list.")
        super().__setitem__(key,value)

    def __contains__(self, item):
        print("You can search an item in list.")
        return super().__contains__(item)


data = MyDictionary({"firstname": "Serhat", "lastname":"Karaarslan"})

print(data)

print(data["firstname"])
print(data["lastname"])

result = data["age"]  # Assign the result to a variable
print(f"Result of accessing 'age': {result}")

data["firstname"] =  "David"

print(result)

print("a" in data)