numbers = [1,5,7,9,45,456,34,73]
letters = ["e","b","a","s","k","l","e","b","a"]

result = min(numbers)   #1
print(result)

result = max(numbers)   #456
print(result)

result = min(letters)   #a
print(result)

result = max (letters)   #s
print(result)

numbers.append(33)    #to add 33 on the last
print(numbers)

numbers.insert(3,10)  #to add 10 in index 3
print(numbers)

numbers.pop()         #to delete the last element on the list
print(numbers)

numbers.pop(3)        #we can give index number too
print(numbers)

letters.remove("l")   #to remove an element with value
print(letters)

numbers.sort()
result = numbers
print(result)

letters.sort()
result = letters
print(result)

numbers.reverse()
result = numbers
print(result)

result = numbers.count(1)
print(result)

print(numbers.index(5))

print(letters.index("a"))

numbers.clear()
print(numbers)