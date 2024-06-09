import requests
import json
import sys
import pdb

##pdb.set_trace()


def bring_current_value():
    try:
        full_json=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        price=float(full_json['bpi']['USD']['rate_float'])
    except requests.RequestException:
        sys.exit(0)
    return price

def calculate_cost(price,number_of_bitcoins):
    cost=price*number_of_bitcoins
    return cost

def main():

    try:
        number_of_bitcoins=float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")
    cost=calculate_cost(bring_current_value(),number_of_bitcoins)
    print(f"${cost:,.4f}")

if __name__=="__main__":
    main()
