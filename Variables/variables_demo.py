#I write the indormation a student with variables
name = "Serhat"
surname = "Karaarslan"
name_surname = name +" "+ surname
number = 123239
gender = "M"
birthday = "23.04.1994"
adress = "Gereonstraße 6"
age = 30

print("The information of that student")
print("Name-Surname : ",name_surname)
print("Number : ",number)
print("Gender : ",gender)
print("Birthday : ",birthday)
print("Adress : ",adress)
print("Age : ",age)


# Products and their costs with tax

productA = 50
productB = 60.5
productC = 356.45 

tax = 0.19

costWithoutTax = (productA+productB+productC) 
costWithTax = costWithoutTax + costWithoutTax*tax

print("The cost of product A : ",productA+productA*tax)
print("The cost of product B : ",productB+productB*tax)
print("The cost of product C : ",productC+productC*tax)

print("The cost of three Products without tax : ",costWithoutTax)
print("The cost of three Products with tax : ",costWithTax)