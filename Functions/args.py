def summe(a,b):
    return a+b

def summe(a,b,c):
    return a + b +c

numbers = [10,20,30,40,50]

# If we want to give parameters to a function,however we dont know how many parameters,
# we can use a list an send the list as a parameter to function
def summe1(list):  
    result = 0
    for i in list:
        result += i
    return result

print(summe1(numbers))


#Other method is the using args

def sum1(*args): #star respresents that we send parameters althought we dont how many
    print(type(args))
    print(args)
    result = 0
    for i in args:
        result += i
    return result

print(sum1(10,20,30))
print(sum1(10,20,30,40,50,60))
