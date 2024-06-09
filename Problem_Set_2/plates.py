import string
##import pdb; pdb.set_trace()



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    letters_counter=0
    numbers_counter=0

    if len(plate)>1 and len(plate) <=6 and has_punctuation(plate)==False:

        while True:

            if plate[letters_counter].isdigit()==False and  letters_counter < len(plate):
                letters_counter += 1
                if letters_counter == len(plate):
                    return True
            elif plate[letters_counter].isdigit()==True:
                break
            else:
                return False

        if letters_counter>1 and plate[letters_counter]!='0':

            while True:

                if plate[letters_counter+numbers_counter].isdigit()==True and  letters_counter+numbers_counter < len(plate):
                    numbers_counter+=1
                    if letters_counter+numbers_counter == len(plate):
                        return True
                else:
                    return False
        else:
            return False
    else:
        return False


def has_punctuation(value):
    has=False

    for _ in value:
        if _ in string.punctuation or _ ==' ':
            has=True
            break

    return has


main()

