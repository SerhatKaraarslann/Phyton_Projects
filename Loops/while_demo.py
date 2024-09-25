numbers = [ 1,2,3,4,5,6,7,8,9,0]

#1-Print the numbers list with while loop
i = 0

while i < len(numbers):
    print(numbers[i])
    i+=1

while numbers:
    print(numbers.pop(0))

#2-Take the start and end numbers and print all of odd numbers between them.

start = int(input("Give the start number : "))
end = int(input("Give the end number : "))

while start <= end:
    if(start%2 == 1):
        print(start)
    start += 1

#3- print the all numbers between 1-100 reverse

i = 100

while(i>=1):
    print(i)
    i -= 1

#4-Print the 5 number, that you take from user

numbers2 = []
i = 0
while(i<5):
    number = int(input("Enter a number : "))
    numbers2.append(number)
    i+=1

numbers2.sort()
print(numbers2)