# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# Question
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

first_sunday_month = 7
years = [x for x in range(1900,2001,1)]
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
sundays = []
first_sunday_month_list = [first_sunday_month]
for y in years:
    if y % 2 == 0 and (y - 1900)%4==0:
        days_in_month[1] = 29
    else:
        days_in_month[1] = 28

    for d in days_in_month:
        if d - first_sunday_month < 28:
            sundays.append(4)
        else:
            sundays.append(5)
        first_sunday_month = 7 - ((d-first_sunday_month)%7)
        first_sunday_month_list.append(first_sunday_month)

print(sum(sundays[12:]))

# check
# import pandas as pd
# print(sum([1 for d in pd.date_range('1901-01-01', '2001-01-01') if d.weekday()==0]))
