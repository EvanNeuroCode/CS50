amount_due=50
change_owed=0
print('amount due: '+ str(amount_due))
new_coin= int(input('insert coin: '))

while amount_due>0:
    if new_coin==25 or new_coin==10 or new_coin==5:
        amount_due=amount_due-new_coin
    if amount_due >0:
        print('Amount Due: '+ str(amount_due))
        new_coin= int(input('insert coin: '))



change_owed=amount_due*-1
print('Change Owed: ' + str(change_owed))
