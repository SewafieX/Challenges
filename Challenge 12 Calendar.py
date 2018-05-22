import calendar
''' This is to print the calendar for January of the year 2020 with Monday as the first day of the week '''
year = int(input("Input the year: "))
month = int(input("Input the month: "))
c = calendar.TextCalendar(calendar.MONDAY)  # Sunday is the first day of the month
# c = calendar.month(year, month)
str = c.formatmonth(year, month)  # Year and month
print(str)
