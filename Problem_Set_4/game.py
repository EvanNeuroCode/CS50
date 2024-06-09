import random

while True:
    try:
        level= int(input("Level: "))
        if level>0:
            break
    except ValueError:
        pass


goal=random.randint(1, int(level))

while True:

    while True:
        try:
            guess=int(input("Guess: "))
            if 1<=int(guess)<=level:
                break
        except ValueError:
            pass

    if guess > goal:
        print("Too large!")
    elif guess < goal:
        print("Too small!")
    else:
        print("Just right!")
        break
