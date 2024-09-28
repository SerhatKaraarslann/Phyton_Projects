#arguments, parameters

def full_name(firstname, lastname):  #parameters
    return f"Your name is {firstname} {lastname}"

result = full_name("Serhat","Karaarslan") #arguments

print(result)

result = full_name(lastname = "Karaarslan",firstname = "Serhat") # we can define arguments like that too
print(result)