import pdb
from datetime import datetime



months_string={
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

##pdb.set_trace()

while True:

    try:

        date=input("Date: ").strip()

        if date[0].isdigit()==False and "," in date:

            date_splitted=date.split(" ")##split here
            year=date_splitted[2]
            month=months_string[date_splitted[0]]
            day=date_splitted[1].replace(",","")


        else:

            month, day, year=date.split("/")##split here

        if int(month)>1 and int(month)<12 and int(day) <31:
            break

    except (ValueError,IndexError) as ErrorDeInput:
        pass

if len(str(month))==1:
    month="0"+str(month)
if len(str(day))==1:
    day="0"+str(day)

result=year+"-"+str(month)+"-"+str(day)

print(result)
