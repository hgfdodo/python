months=['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Act','Nov','Dec']
endings=['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] + 7*['th'] + ['st']
year=raw_input("Year:")
month=raw_input("Month:")
day=raw_input("Day:")
month_number = int(month)
day_number= int(day)
month_p = months[month_number-1]
day_p = day+endings[day_number-1]
print ( month_p+ " " + day_p + ", " +year)