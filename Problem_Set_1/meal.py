import pdb

def main():
    current_time= input('What time is it? ')

    current_time=convert(current_time)

    if current_time>=7 and current_time<=8:
        result='breakfast time'
    elif current_time>=12 and current_time<=13:
        result='lunch time'
    elif current_time>=18 and current_time<=19:
        result='dinner time'
    else:
        result=''

    print(result)

def convert(time):
    time=time.split(':')
    minutos=int(time[1])/60
    time=float(time[0])+float(minutos)
    return time


if __name__ == "__main__":
    main()
