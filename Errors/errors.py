#error
#Error handling in Python like in Java, instead of try catch block there are try and except block hier.
#try block is specific for the codes and show us, how should start the program without errors 
#in the except block we re handling the error and is shown us which message with error we accept 

#error handling
try:
    x = int(input("x : "))
    y = int(input("y : "))

    print(x+y)

except: 
    print("There is an error!")