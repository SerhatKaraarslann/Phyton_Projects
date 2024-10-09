#in try we write the codes, that possibly cause an error

try: 
    x = int(input("x : "))
    y = int(input("y :"))

    print(x/y)

except ZeroDivisionError: # we can give hier the exception type and this block start just when it meets with this typ of error
    print("y can't be Zero!")
except ValueError:
    print("X and y must be number!")
except:  # if we write like this, that is for all of error types
    print("There is an error!")