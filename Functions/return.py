def summe():
    return f"Summe : {10+20}"

a = summe()
print(a)

print(summe())
 
def now1():
    import datetime
    return datetime.datetime.now().year
    

def cakculateAge():
    return now1() - 1983

result = cakculateAge()
print(result)

def now2():
    import datetime
    return datetime.datetime.now().hour
    


def greet():
    if(now2() < 12):
        return "Morning, Serhat"
    else:
        return "Hi, Serhat"
    
result = greet()

print(result)