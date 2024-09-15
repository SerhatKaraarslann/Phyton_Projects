webseite = "http:// www.fh-muenster.de"
course = "Python Course: From Zero to Hero"

# 1- Erase the space on the start and end of str
str = " Hello World "

s =  str.strip()
print(s)

#2-Erase the all of character in the webseite except fh-muenster

result = webseite.strip(webseite[0:10]).strip(webseite[len(webseite)-3:])
print(result)

#3- Make lower all character on the course name

result = course.lower()
print(result)

#4-How many e is there in the webseite
result = webseite.count("e")
print(result)

#5- Webseite does start with "http" and end with "de"?

result = webseite.startswith("h")
print(result)
result = webseite.endswith("de")
print(result)

#6- Does webseite have any "de" in?
result = bool(webseite.find(".de"))
print(result)

#7-Does all character in course alphabetic?

result = webseite.isalpha()
print(result)

#8- center the "contents" in line with 50 characters, that are right and left sides with "*".

result = "Contents".center(50,"*")
print(result)

result = "Contents".ljust(50,"*")
print(result)

result = "Contents".rjust(50,"*")
print(result)

#9- Change the all space in course with "-".

result = course.replace(" ","-")
print(result)

#10- Replace the "World" in the "Hello World" with "There"

result = str.replace("World","There")
print(result)

#11- Split the Course characters with space.

result = course.split(" ")
print(result)