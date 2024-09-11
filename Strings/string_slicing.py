"""
Strings is in python like an array, character array.
That's why we can slice them and reach some part of the string.
"""

msg = "My name is Serhat and i love Python!"

print(msg[0])   #M
print(msg[-5])  #t

print(msg[-7:-1]) #Python

print(len(msg))  #length of message = 36.

print(msg[0:5])  #My na

print(msg[:10])  # That means msg[0:10] literally : My name is 

print(msg[5:])   # That means msg[5:end] literally :me is Serhat and i love Python!

print(msg[0:30:2])  #not the all character, every second character pass : M aei ehtadilv

print(msg[::-1])   #reverse