inputed=input('Input: ')
outputed=''
for _ in inputed:
    if _.lower() in ['a','e','i','o','u']:
        continue
    else:
        outputed=outputed+_
print('Output: ' + outputed)
