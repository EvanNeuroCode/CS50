##import pdb
##pdb.set_trace()



def input_the_info():

    current_fuel= input("Input your fuel as a fraction: ").split("/")

    ##To use this variables after the function
    global x,y
    ##defining the denominator and numerator
    try:
        x=current_fuel[0]
        y=current_fuel[1]
    except IndexError:
        print("separator is probably not a slash")
        input_the_info()
    ##Ensuring they are integers and separator is a slash:
    try:
        x=int(x)
        y=int(y)
    except ValueError:
        print("the numerator and/or denominator are not integers")
        input_the_info()
    ##ensuring the numerator is not bigger than the denominator
    if x>y:
        print("Numerator is bigger than denominator")
        input_the_info()
    else:
        return x,y

input_the_info()

##ensuring there is no zero in the denominator and the values are numbers
invalid=True
while invalid==True:

    try:
        fuel_gauge=round((int(x)/int(y))*100)
        invalid=False
    except ZeroDivisionError:
        print("there is a zero in the denominator")
        input_the_info()
    except ValueError:
        print("those are not numbers")
        input_the_info()

#validating if it's empty or full
if fuel_gauge<=1:
    print("E")
elif fuel_gauge >=99:
    print("F")
else:
    print(str(fuel_gauge)+'%')
