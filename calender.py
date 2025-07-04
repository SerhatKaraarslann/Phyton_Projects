import calendar

for i in range(1900,2025):
    yy = i

    for k in range(1,13):
        mm = k

       #display the calendar
        print(calendar.month(yy,mm))