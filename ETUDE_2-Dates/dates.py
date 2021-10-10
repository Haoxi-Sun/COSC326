# Elsie Sun 4468203
#
# Using an Algorithm of the leap year from:
# https://en.wikipedia.org/wiki/Leap_year#Algorithm
#
# I am assuming the program will stop and show an error message
# if one of the formats, days, months, or years is invalid
# it output a correct date if all data are valid
import fileinput

# store error messages
def error_messages(error):
    if error == "separator":
        print(date_string+" - INVALID: Separator is invalid.")

    elif error == "year":
        print(date_string+" - INVALID: Year is invalid.")

    elif error == "month":
        print(date_string+" - INVALID: Month is invalid.")

    elif error == "day":
        print(date_string+" - INVALID: Day is invalid.")

# determine whether or not it is a leap year
def isLeap(year_string):
    if (int(year_string) % 4 == 0 and int(year_string) % 100 != 0) or (int(year_string) % 400 == 0):
        return True
    return False

# determine whether or not the day is valid
def day_check(year_string,month_string,day_string):
    global months, days_in_months_leap, days_in_months
    if len(day_string) > 2: return False
    try:
        # if this year is a leap year
        # there are 29days in Feb
        if isLeap(year_string) == True:
            if month_string in months:
                index = months.index(month_string)
                if 1 <= int(day_string) <= days_in_months_leap[index]:
                    return True
                else:
                    return False

        # if is not a leap year
        else:
            if month_string in months:
                index = months.index(month_string)
                if 1 <= int(day_string) <= days_in_months[index]:
                    return True
                else:
                    return False
    except ValueError:
        return False

# determine whether or not the month is valid
def month_check(month_string):
#    month_num = [1,2,3,4,5,6,7,8,9,10,11,12]
    # if the month is a short form
    if len(month_string) == 3:
        if month_string.isalpha():
            # check a format of the month
            if month_string.isupper() or month_string.islower():
                month_lower = month_string.lower().capitalize()
            elif month_string[0].isupper() and month_string[1:].islower():
                    month_lower = month_string
            else:
                return False
            if month_lower in months:
                return True
        return False

    # if the month is not a short form
    # is a number
    if len(month_string) <= 2:
        if month_string.isdigit():
            if int(month_string) in range(1,13):
                return True
            return False
        return False
    return False

# determine whether or not the year is valid
def year_check(year_string):
    if len(year_string) == 4:
        if 1753 <= int(year_string) <= 3000:
            return True

    return False

# determine whether or not the separator type is valid
# if there are two different separator types used in one date
def separator_check(date_string):

    num_space = 0
    num_slash = 0
    num_hyphen = 0

    for i in date_string:
        if i == " ": num_space += 1
        if i == "-": num_hyphen += 1
        if i == "/": num_slash += 1
    
    if num_space == 2 or num_slash == 2 or num_hyphen == 2:
        return True
    return False
    

print("Please enter a date: ")

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days_in_months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for line in fileinput.input():
    date_string = line.replace("\n","")011

    # check separators
    if separator_check(date_string) == False:
        error_messages("separator")

    else:
        if " "in date_string :
            date = date_string.split(" ")
        elif "/" in date_string:
            date = date_string.split("/")
        elif "-" in date_string:
            date = date_string.split("-")

        day = date[0]
        month = date[1]
        year = date[2]

        # check the year
        if len(year) == 2:
            if int(year) >= 50:
                year = "19"+str(year)
            elif int(year) <= 49:
                year = "20"+str(year)
                                  
        if year_check(year) == False:
            error_messages("year")
        else:
            
            # check the month
            if month_check(month) == False:
                error_messages("month")
            elif month_check(month) == True:
                if month.isdigit():
                    month = months[int(month)-1]
                elif month.isalpha():
                    month = month.lower().capitalize()

                # check the day
                if day_check(year, month, day) == False:
                    error_messages("day")
                else:
                    if len(day) == 1:
                        day = "0"+day

        if year_check(year) == True and month_check(month) == True and day_check(year,month,day) == True:
            print(day+" "+month+" "+year)

    print("Please enter a date: ")
