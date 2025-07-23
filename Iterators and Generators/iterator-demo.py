def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            number = next(iterator)
            func(number)
        except StopIteration:
            break


numbers = [1,2,3,4,656,74,22,45,78,27,5321,467,24,1245673]
s = "It's fantastic to write code in python!"

my_for(numbers,print)
my_for(s,print)

def square(x):
    print(x*x)

my_for(numbers,square)