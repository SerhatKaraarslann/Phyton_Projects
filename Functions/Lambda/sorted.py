numbers = [1,5,3,45,67,53,7]

#numbers.sort()  #to sort the list
# the diffence betwwen these two funcitons are with sorted, the original list doesnt change, but with sort function it changes 
result = sorted(numbers) 
print(result)    #[1, 3, 5, 7, 45, 53, 67]
print(numbers)   #[1, 5, 3, 45, 67, 53, 7]

result = sorted(numbers,reverse = True)  #[67, 53, 45, 7, 5, 3, 1]
print(result)

result = sorted(([1, 5, 3, 45, 67, 53, 7]))  #we save the tuple in result
print(result)

users = [
    {    "username":"Serhat Karaarslan","tweets":["tweet1","tweet2","tweet3"],"email" : "karaarslan234qgmail.com"},
    {    "username":"Ferhat Karaarslan","tweets":["tweet1","tweet2"]},
    {    "username":"Julia Penner","tweets":[],"name" : "","phone":"+4915473864387"}
]

result = sorted(users, key = len) # here we sorted the list according to key lengths
print(result)

print("#################################################")

result = sorted(users,key = len, reverse = True)
print(result)
print("#################################################")

result = sorted(users,key = lambda user : (user["username"]))   ## here we sorted the list according to username as alphabetic
print(result) 
print("#################################################")

result = sorted(users,key = lambda user : len(user["tweets"]))   ## here we sorted the list according to username as alphabetic
print(result) 
print("#################################################")

courses = [
    { "title" : "Python Course", "students" : 25000 },
    { "title" : "Web Development", "students" : 21000 },
    { "title" : "Java Course", "students" : 27000 }
]

result = sorted(courses, key = lambda course : course["students"] ,reverse = True)  # according to most populer course(studentsnumbers)
print(result)
print("#################################################")

result = map(lambda course : course["title"],sorted(courses, key = lambda course: course["students"],reverse = True))
print(list(result))