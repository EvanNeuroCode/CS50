import pdb
##pdb.set_trace()
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
   ## pdb.set_trace()
    tip = dollars * percent
    ##pdb.set_trace()
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    ##pdb.set_trace()
    d=float(d.replace("$",""))
    return d


def percent_to_float(p):
     ##pdb.set_trace()
     p=float(p.replace("%",""))/100
     return p

main()
