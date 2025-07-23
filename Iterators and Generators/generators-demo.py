# We write a function to get every numbers square between 1 - infinity
# We can do that with normal way, so much memory we need for it

def infinity_number():
    number = 0
    while True:
        yield number * number
        number += 1

generator = infinity_number()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

#for i in generator: # now its an inifinity loop
#    print(i)


# Fibonacci series with normal way and with generator

def fib_list(max):
    numbers = []
    a,b = 0,1
    while len(numbers) < max:
        numbers.append(b)
        a,b = b, a+b
    return numbers

print(fib_list(10))


def fib_gen(max):
    a,b = 0,1
    count = 0
    while count < max:
        a,b = b,a+b
        yield b
        count += 1



#for i in fib_gen(100000):
#    print(i)


import sys

list1 = [i*2 for i in range(10000)] 
print(sys.getsizeof(list1)) # this method show us the memory size # 85176

gen = (i**2 for i in range(100000000)) 
print(sys.getsizeof(gen)) # just 200

gen = (i**2 for i in range(1000000000000000)) 
print(sys.getsizeof(gen)) # again 200, doesnt matter how big is the gen size

import time 

list_start_time = time.time()
sum([i**2 for i in range(10000000)]) 
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum(i**2 for i in range(10000000)) 
gen_stop = time.time() - gen_start_time

print(list_stop)
print(gen_stop)

#generators are more effectiver als normal use