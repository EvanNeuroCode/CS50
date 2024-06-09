values = input('Type your equation: ').split()
x=int(values[0])
y=values[1]
z=int(values[2])

if y=='+':
    result= x+z
elif y=='-':
    result= x-z
elif y=='*':
    result= x*z
elif y=='/':
    result= x/z
else:
    result='qué operador es ese, hombre!?'
    print(result)
    exit()

print(float(result))
