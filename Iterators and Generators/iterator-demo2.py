class Counter:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self): # With this method we can convert our object in an iterable object
        return self # return self makes it.

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        

for i in Counter(10,20):
    print(i)

iterator = iter(Counter(10,20))
print(next(iterator))

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break