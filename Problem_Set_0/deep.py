question= input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if question=='42':
    result='Yes'
elif question=='forty-two' or question=='forty two':
    result='Yes'
else:
    result='No'
print(result)
