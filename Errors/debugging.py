import pdb  # we have to import this library to debugging

one = "one"
two = "two"

pdb.set_trace()  # this method is to stop the program on this line and see the parameters/other things

result = one + two

three = "Three"

result += three

print(result)



def add_numbers(a,b,c):
    import pdb;pdb.set_trace()
    return a+b+c


#l => list
#n => next line
#p => print
#c => continue