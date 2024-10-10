list1 = ["1","2","5a","10b","abc","20","500"]

#1- find the numbers in the list


for x in list1:
    try:
      result = int(x)
      print(result)
    except ValueError:
      continue

        

#2- Make sure that every input you receive is a numeric value unless the user enters a q value, otherwise you will get an error message.

while True:
    number = input("number : ")
    if(number == "q"):
      break
   
    try:
        result = float(number)
        print(f"Number : {result}")
        break
    except ValueError:
       print("Unacceptable value")
       continue



#3- Write a function that takes Dictionary and key infos as a paramater. get(d,key)

product = {"productname" : "Samsung S23"}
    #d["price"] => KeyError
    #get(d,"price") => None
    #get(d,"productname") => "Samsung S23"

def get(d,key):
   try:
        return d[key]
   except KeyError:
        return None
   
print(get(product,"price"))
print(get(product,"productname"))
      