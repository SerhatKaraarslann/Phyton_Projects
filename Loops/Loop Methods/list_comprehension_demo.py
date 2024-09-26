names = ["Ferhat","Serhat","Uras","Nora","Isa","Havva"]
string = "Hello 12345 World"
years = [1983,1999,2008,1956,1986]
degrees = [20,5,15,-2,0,-7]

#1- Make a list, which includes the numbers, that are between 1-100 and divided by 12.

numbers = [number for number in range(1,100) if(number%12==0)]
print(numbers)

#2- print reverse every element of names list with lower letter.

namesRev = [name.lower()[::-1] for name in names ]
print(namesRev)


#3-make a list, which includes the elements of stringlist

list1 = [letter for letter in string if(letter.isdigit())]
print(list1)

#4-Make a list that includes the age of person, who was born in the year of the yearslist.

ages = [2024-year for year in years]
print(ages)

#5-Print "Attention! Icing Danger" for the elements of the degrees list, that under 4 degrees.

degrees1 = [degree if(degree>4) else "Attention! Icing danger" for degree in degrees ]

print(degrees1)