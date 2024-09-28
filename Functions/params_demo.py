#1- Make a function that prints the larger of two parameters sent to it

def findMax(number1,number2):
    if(number1 > number2):
        return number1
    elif(number1 < number2):
        return number2
    else:
        return f"The numbers are equal."

result = findMax(10,23)
print("The max of two numbers is :{} ".format(result))


#2- Write a function that finds the number of times each character is repeated in a string of information sent to it.

def findChar(str):
    return {letter : str.count(letter) for letter in str}

result = findChar("Serhat Karaarslan")
print(result)
        

#3-update the list according to the list, command, position and value fields sent to it.

def update_list(list, command, position, value = None):
    if(command == "remove" and position == "end"):
        return list.pop()
    elif(command == "remove" and position == "beginning"):
        return list.pop(0)
    elif(command == "add" and position == "end"):
        list.append(value)
        return list
    elif(command == "add" and position == "beginning"):
        list.insert(0,value)
        return list

result = update_list([1,2,3],"add","end",4)
print(result)

result = update_list([1,2,3,4,5],"add","beginning",65)
print(result)

result = update_list([1,2,3,4,5],"remove","beginning")
print(result)

result = update_list([1,2,3,4,5],"remove","end")
print(result)


#4- Write a function that returns True if the color “blue” is in the color names sent to it.

def contains_blue(*args):
    if "blue" in args:
        return True
    return False
    

result = contains_blue("yellow","red","blue","green")
print(result)

result = contains_blue("yellow","red","black","green")
print(result)