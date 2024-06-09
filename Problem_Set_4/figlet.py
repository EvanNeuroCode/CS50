from pyfiglet import Figlet
import random
import sys

figlet=Figlet()


if len(sys.argv)==1:
    text= input("Input: ")
    font1=random.choice(figlet.getFonts())
elif len(sys.argv)==3:
    if sys.argv[1] not in ("-f","--font") or sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        text= input("Input: ")
        font1=sys.argv[2]
else:
    sys.exit("Invalid usage")


figlet.setFont(font=font1)
print("Output: " + figlet.renderText(text))
