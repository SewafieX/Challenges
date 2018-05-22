from datetime import date

d1 = date(2009, 10, 17)
d2 = date(2008, 8, 20)
tdelta = d1 - d2
print(tdelta.days)
