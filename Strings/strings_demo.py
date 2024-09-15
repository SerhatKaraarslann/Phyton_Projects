webseite = "http://www.fh-muenster.de"
course = "Python Course: From Zero to Hero"

lenght = len(course) #32
print("The lenght of string course {}.".format(lenght))

print(webseite[7:10]) #www

lenght2 = len(webseite)
print(webseite[lenght2-2:])  #de

print(course[0:15], course[lenght-15:])


print(course[::-1])


str = "Hello world"
s = str[0:6] + "W" +str[-4:]

print(s)

x= "abc"
print(x*3)


