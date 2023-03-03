from datetime import date

def DaysToNewYear(*dates):
    for date_today in dates:

        date_end_year = date(date_today.year, 12, 31)
        delta = date_end_year - date_today
        print(delta)

print(DaysToNewYear(date(1998,12,5),date(1998,12,1)))

