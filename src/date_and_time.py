from datetime import date, datetime

# Current date
def date_today():
    day = str(date.today())
    # print("Today's date:", today)
    today_lst = day.split("-")[::-1]
    strn = ""
    if today_lst[0] == 1:
        strn += today_lst[0] + "st "
    elif today_lst[0] == 2:
        strn += today_lst[0] + "nd "
    elif today_lst[0] == 3:
        strn += today_lst[0] + "rd "
    else:
        strn += today_lst[0] + "th "
    
    if int(today_lst[1]) == 1:
        strn += "January "
    elif int(today_lst[1]) == 2:
        strn += "February "
    elif int(today_lst[1]) == 3:
        strn += "March "
    elif int(today_lst[1]) == 4:
        strn += "April "
    elif int(today_lst[1]) == 5:
        strn += "May "
    elif int(today_lst[1]) == 6:
        strn += "June "
    elif int(today_lst[1]) == 7:
        strn += "July "
    elif int(today_lst[1]) == 8:
        strn += "August "
    elif int(today_lst[1]) == 9:
        strn += "September "
    elif int(today_lst[1]) == 10:
        strn += "October "
    elif int(today_lst[1]) == 11:
        strn += "November "
    else:
        strn += "December "
    return strn+str(today_lst[2])


# Current time
def current_time():
    current_time = str(datetime.now().time()).split('.')[0].split(':')
    current_time = f"{current_time[0]} hours, {current_time[1]} minutes and {current_time[2]} seconds"
    return current_time


# Weekday
def weekday():
    day = datetime.today().weekday()
    if day == 0:
        return "Monday"
    elif day == 1:
        return "Tuesday"
    elif day == 2:
        return "Wednesday"
    elif day == 3:
        return "Thursday"
    elif day == 4:
        return "Friday"
    elif day == 5:
        return "Saturday"
    else:
        return "Sunday"

# print(date_today())
# print(weekday())
# print(current_time())