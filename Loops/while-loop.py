numbers = [1,2,3,4,5,6,7,8,9,]

#for => collection
#while => condition 

i = 0
while i < 10:  #infinite loop
    print("Hallo")
    i += 1    # 10 times now 


username = ""

print(bool(username)) #false

username = "a"

print(bool(username))  #true


username = ""
while not username:
    username = input("Username :")

print("Your username :",username)