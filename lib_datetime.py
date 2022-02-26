import datetime

today = datetime.date.today()

print(today)
print(type(today))

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("date1 =", d1)

# tekstowo miesiac, potem dzień i rok
d2 = today.strftime("%B %d, %Y")
print("date2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("date3 =", d3)

# tekstowo skrócony miesiac, potem dzień i rok
d4 = today.strftime("%b-%d-%Y")
print("date4 =", d4)

now = datetime.datetime.now()
print(now)
print(type(now))

my_time = now.strftime('%H:%M:%S')
date = now.strftime('%Y-%m-%d')
print('\n Time now is ',my_time)
print('Date now is ',date)
