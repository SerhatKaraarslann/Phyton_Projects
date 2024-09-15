msg = "Welcome to our Python Class. Do you love Python?"

msg = msg.upper()  #WELCOME TO OUR PYTHON CLASS! DO YOU LOVE PYTHON?
print(msg)

msg = msg.lower()  #welcome to our python class! do you love python?
print(msg)

msg = msg.title()  #Welcome To Our Python Class! Do You Love Python?
print(msg)

msg = msg.capitalize()   #Welcome to our python class! do you love python?
print(msg)

result = msg.islower()
print(result)
result = msg.isupper()
print(result)


msg2 = "                    xyz                   "
result = msg2.strip()
print(result)

result = msg.split()
print(result)

print(result[2])

result = msg.split(".")
print(result)

result = msg.split()
result = "---".join(result)
print(result)


index = msg.index("class")
print(index)

result = msg.replace("python","Java")
print(result)

