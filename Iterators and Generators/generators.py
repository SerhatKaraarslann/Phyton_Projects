# Generator function which creates iterable objects.
# A generator is a special type of iterator that yields values one at a time using the yield keyword,
# instead of returning them all at once like a list.

# Lazy: They produce items only when requested.
# Memory-efficient: They don’t store the entire sequence in memory.
# Used in loops or with functions like next().

# In this function we write the elements in a list, thats for big data no efficient. 
def get_numbers(max):
    number = 1
    numbers = []
    while number <= max:
        numbers.append(number)
        number += 1
    return numbers

result = get_numbers(10)
print(result)

# Instead of write in memory space with generators we can take results without writing in a special memory space
# We dont need the return this data
def get_numbers2(max):
    number = 1
    while number <= max:
        yield number
        number += 1

# we have to use next method now
generator = get_numbers2(10) # now tis a generator object
print(next(generator)) #First element now. After print we can reach this element now, we didnt write in a memory space like list or something like that.

while True:
    try:
        print(next(generator))
    except StopIteration:
        break


generator2 = (i for i in range(1,11)) # we can use it with list comprehension 

print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
