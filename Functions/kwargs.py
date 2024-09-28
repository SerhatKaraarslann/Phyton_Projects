def displayUser(*args):
    print(type(args))   #tuple
    print(args)

displayUser()

def displayUser(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print("\n")

   # print(type(kwargs))  #dictionary
   # print(kwargs)

displayUser(username = "Serhat Karaarslan")
displayUser(username = "Serhat Karaarslan", email = "karaarslan234@gmail.com",country = "Germany")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value1",key2="value2")

myFunc(10,20,30,key = "value")