salutation=input('Greeting: ')
if 'hello' in salutation.lower():
    result='$0'
elif 'h' in salutation[0].lower():
    result='$20'
else:
    result='$100'

print(result)

