from datetime import datetime

date_time = '2022-04-07T21:58'

date = date_time[:10]
time = date_time[11:]
print(date)
print(time)

mydate = datetime.strptime(date, "%Y-%m-%d")
print(mydate.month)
print(mydate.strftime("%A")),
print(mydate.strftime("%d"))
print(mydate.strftime("%B"))
print(mydate.strftime("%Y"))
print(time)
# print('Day of Month:', calendar.day_name[mydate.month()])