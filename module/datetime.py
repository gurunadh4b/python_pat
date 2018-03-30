import datetime as dt
date1=dt.date(2017,12,14)
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)

time1=dt.time(10,45,12,4578) #hr min sec msec
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)

datetime1=dt.datetime(2018,03,24,10,45,12,1458)
print(datetime1)
print(datetime1.hour)


import  time as t
print(t.localtime())
print(t.gmtime())
print(t.asctime())
print('hhhhhhhhhhh')

print(date1.isoweekday())