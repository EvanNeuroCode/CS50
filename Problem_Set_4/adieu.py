import inflect

l = inflect.engine()
my_list=[]

while True:

    try:
        my_list.append(input("Name: "))
    except EOFError:
        print()
        break

result = l.join(my_list)
print("Adieu, adieu, to", result)
