

grocery_list={}

while True:
    try:
        item= input("").upper()
        if item in grocery_list:
            grocery_list[item]=grocery_list[item]+1
        else:
            grocery_list[item]=1

    except EOFError:
        print("\n")
        break

sorted_grocery_list=dict(sorted(grocery_list.items()))

for _ in sorted_grocery_list:
    print(sorted_grocery_list[_], _, end="\n")
