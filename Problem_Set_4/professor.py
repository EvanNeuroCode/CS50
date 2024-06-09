import random
import sys
import pdb

##pdb.set_trace()
matrix_values = []

def main():
    get_level()
    generate_integer(level)
    ##pdb.set_trace()
    score=0
    for i in range(10):
        errors=0
        while errors<3:
            answer=matrix_values[i][0]+matrix_values[i][1]
            equation=str(matrix_values[i][0])+" + "+str(matrix_values[i][1])+" ="
            guess=int(input(equation))
            if guess==answer:
                correct=True
                score+=1
                break
            else:
                correct=False
                errors+=1
                print("EEE")
        if (errors==3 or guess==answer) and correct==False:
            print(equation+str(answer))

    print("Score: "+str(score))
    sys.exit(0)

def get_level():
    global level
    while True:
        try:
            level=int(input("Level: "))
            if level in (1,2,3):
                break
        except ValueError:
            pass

def generate_integer(level):
    global matrix_values
    matrix_values = []  # Initialize matrix_values as an empty list
    for _ in range(10):  # For each row in the matrix
        if level==1:
            row = [random.randint((10**(level-1))-1, (10**level)-1) for _ in range(2)]
        else:
            row = [random.randint((10**(level-1)), (10**level)-1) for _ in range(2)]
        matrix_values.append(row)



if __name__ == "__main__":
    main()
