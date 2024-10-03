def multiply(a):
    return a**2

print(multiply(4))  # 4*4 = 16

result = lambda a : a**2 # lambda parameter : result values

print(result(4))  #16

summe = lambda a,b,c : a+b+c
print(summe(2,3,4))

reverse = lambda str : str[::-1]
result = reverse("Serhat Karaarslan")
print(result)

def myFunc(n):
    return lambda a: a*n

multiply2 = myFunc(2)
multiply3 = myFunc(3)

result = multiply2(10)
print(result)

result = multiply3(30)
print(result)


