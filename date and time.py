from datetime import date
r = int(input('Year: '))
t = int(input('Month: '))
y = int(input('Day: '))
time = date(year=r,month=t,day=y)
time2 = date.today()
b = time2 - time
print('You are',str(time2.year - time.year) , 'years,',str(time2.month - time.month),'months and',str(time2.day - time.day),'days old')
print('Congratulations! You have survived',str(b), 'days on the earth')
print('Congratulations! You have survived',str(b.total_seconds()), 'seconds on the earth')

