import pdb
from emoji import emojize


print(emojize('Python is really cool :thumbs_up:'))

##pdb.set_trace()




emoji= input("Input: ")

try:
    result=emojize(emoji, language='alias')
    print(result)
except:
    pass
