# Make an application, which calculates how much fuel a vehicle costs over a specified distance based on fuel type.

benzinCost = 1.98
dieselCost = 1.86

averageFuelConsum = float(input("Average Fuel Consum in 100 km : "))

wayInKm = float(input("Way in Km : "))

fuelTyp = input("Fuel Typ : ")

amountOfFuelConsum = wayInKm*(averageFuelConsum/100)

if(fuelTyp == "benzin"):
    amountOfCost = benzinCost*amountOfFuelConsum
    print(amountOfCost)
elif(fuelTyp == "diesel"):
    amountOfCost = dieselCost*amountOfFuelConsum
    print(amountOfCost)
else:
    print("Wrong fuel typ!")


