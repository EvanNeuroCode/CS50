import pdb
camelCase= input('camelCase: ')
##pdb.set_trace()
print(camelCase[0].lower())
for _ in range(0,len(camelCase)):
    if _==0:
        result=camelCase[0].lower()
    elif camelCase[_].isupper():
        result=result+'_'
        result=result+camelCase[_].lower()
    else:
        result=result+camelCase[_]
print(result)
