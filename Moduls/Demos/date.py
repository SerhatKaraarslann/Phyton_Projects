#This module is the using date, time 

#import datetime
#result = dir(datetime)
#print(result)

from datetime import datetime
from datetime import timedelta

result = dir(datetime)
print(result)

result = datetime.now()  #actual time 2024-10-13 21:19:46.445331
print(result)

#now we can take the part of that time

result = datetime.now().year #2024
print(result)

result = datetime.now().month #10
print(result)

result = datetime.now().day  #13
print(result)

result = datetime.now().hour  #21
print(result)

result = datetime.now().minute  #22
print(result)

result = datetime.now().second # 19
print(result)

result = datetime.today()  #2024-10-13 21:22:19.638765
print(result)

result = datetime.ctime(datetime.now()) #Sun Oct 13 21:24:16 2024
print(result)

result = datetime.strftime(datetime.now(),"%Y") # 2024
print(result)

result = datetime.strftime(datetime.now(),"%X") # 21:27:03
print(result)

result = datetime.strftime(datetime.now(),"%d") # 13
print(result)

result = datetime.strftime(datetime.now(),"%A") # Sunday
print(result)

result = datetime.strftime(datetime.now(),"%B") # October
print(result)

result = datetime.strftime(datetime.now(),"%Y %b %a") # 2024 Oct Sun
print(result)

t = "21 April 2019"

day1,month1,year1 = t.split()
print(day1)  #21
print(month1) #April
print(year1)  #2019

t2 = "15 April 2019 hour 12:12:30"
dt = datetime.strptime(t2,"%d %B %Y hour %H:%M:%S")  #2019-04-15 12:12:30
print(dt) 

dt = dt.year
print(dt)  #2019

birthday = datetime(1994,4,23,9,5,0)
print(birthday)

result = datetime.timestamp(birthday) # as second 
print(result)

result = datetime.fromtimestamp(result) # from second to datetime object
print(result)

result = datetime.fromtimestamp(0)  # 1970-01-01 01:00:00 this time is the beginning for the computers
print(result)

result = datetime.now() - birthday  #11131 days, 12:33:28.481369
print(result)

#result = result.days
#print(result)

result = result.seconds
print(result)

result = datetime.now()  #2024-10-13 21:42:58.768751
print(result)

result = result + timedelta(days = 10) #2024-10-23 21:42:58.768751
print(result)