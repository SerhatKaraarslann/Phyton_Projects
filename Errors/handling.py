#in try we write the codes, that possibly cause an error

while True:
    try: 
        x = int(input("x : "))
        y = int(input("y :"))
        print(x/y)
    except ZeroDivisionError as e:  # we can give hier the exception type and this block start just when it meets with this typ of error
        print("y can't be Zero!")
        print(e)                   # we can print the error message
    except ValueError:
        print("X and y must be number!")
    except Exception as e:  # if we write like this, that is for all of error types
        print("There is an error!")
        print(e)
    else:  # if there is no error, this block will run
        print("No error")
        break
    finally:  # this block will run in all cases
        print("Finally block")

    