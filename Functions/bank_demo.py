SerhatAccount = {
    "name":"Serhat Karaarslan",
    "accountNo" : "123456789",
    "balance" : 3000,
    "additionalAccount" : 2000
}

HüseyinAccount = {
    "name":"Hüseyin Vicil",
    "accountNo" : "12345678",
    "balance" : 4000,
    "additionalAccount" : 7000
}

def withdrawMoney(account, amount):
    print(f"Welcome {account["name"]}")

    if(account["balance"] >= amount):
        account["balance"] -= amount
        print("You can withdraw your money!")
        queryBalance(account)
    else:
        sum = account["balance"] + account["additionalAccount"]
        
        if(sum >= amount):
            usingAdditionalAccount = input("Do you want to use your additional account?(y/n)")

            if(usingAdditionalAccount == "y"):
                amountToUseAA = amount - account["balance"]
                account["balance"] = 0
                account["additionalAccount"] -= amountToUseAA

                print("You can withdraw the amount!")
                queryBalance(account)
            else:
                print(f"Your account with the number {account["accountNo"]} has {account["balance"]}")
        else:
            print("Your balance is less than amount!")
            queryBalance(account)


def queryBalance(account):
    print(f"In your account with number {account["accountNo"]} has {account["balance"]} Euro."
          f"Your additional Account limit is {account["additionalAccount"]} Euro.")

withdrawMoney(SerhatAccount,3000)

print("******************************************")

withdrawMoney(SerhatAccount,2000)
