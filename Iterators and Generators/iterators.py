# A loop makes the object iterable an calls __iter__() method. We dont see it.
# Sometimes we need the create an iterator to make our loop in our class.
# Because of that is this topic important.

# iterable? 
#An iterable is any Python object that can return its elements one at a time.
#An iterable has an __iter__() method that returns an iterator

# iterator?
#An iterator is an object that represents a stream of data. It returns the next item of the iterable when you call next() on it.
#Has a __next__() method to get the next item.
#Raises StopIteration when there are no more items.
#Is returned by calling iter() on an iterable.

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for i in numbers:
    print(i)

print(dir(numbers))

#print(next(numbers)) # This method give us an error. TypeError: 'list' object is not an iterator

# We have to convert in iterator object which makes for loop for us. for loop calls __iter__() method to convert an object to an iterator object.

iterator = iter(numbers)
print(next(iterator)) #First element of list
print(next(iterator))   #2
print(next(iterator))   #3
print(next(iterator))   #4  
print(next(iterator))   #5


# We can write our loop like this. Except is for the last element of list. After that comes an error. except to avoid this error.
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break