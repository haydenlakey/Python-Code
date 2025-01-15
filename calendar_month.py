#Calendar using functions
#Hayden Lakey
#7 April 2022
#LKYHAY001

import math
def day_of_week(day, month, year):
    if month == "1" or month == "2":
        month += 12
        year -= 1
        h = (day + abs((13*(month+1))/5)+year+abs(year/4)-abs(year/100)+abs(year/400))%7
    else:
        h = (day + abs((13*(month+1))/5)+year+abs(year/4)-abs(year/100)+abs(year/400))%7
    
    h = ((h+5)%7)+1
    h = round(h)
    return h

def is_leap(year):
    if year%4 == 0:
        Boo = True
    else:
        Boo = False
    return Boo

def month_num(month_name):
    if month_name == 'January':
        monthnum = 1
    elif month_name == 'February': 
        monthnum = 2
    elif month_name == 'March':
        monthnum = 3
    elif month_name == 'April':
        monthnum = 4
    elif month_name == 'May':
        monthnum = 5
    elif month_name == 'June':
        monthnum = 6
    elif month_name == 'July':
        monthnum = 7
    elif month_name == 'August':
        monthnum = 8
    elif month_name == 'September':
        monthnum = 9    
    elif month_name == 'October':
        monthnum = 10
    elif month_name == 'November':
        monthnum = 11
    elif month_name == "December":
        monthnum = 12
    elif month_name == 'january':
        monthnum = 1
    elif month_name == 'february': 
        monthnum = 2
    elif month_name == 'march':
        monthnum = 3
    elif month_name == 'april':
        monthnum = 4
    elif month_name == 'may':
        monthnum = 5
    elif month_name == 'june':
        monthnum = 6
    elif month_name == 'july':
        monthnum = 7
    elif month_name == 'august':
        monthnum = 8
    elif month_name == 'september':
        monthnum = 9    
    elif month_name == 'october':
        monthnum = 10
    elif month_name == 'november':
        monthnum = 11
    elif month_name == "december":
        monthnum = 12      
    elif month_name == 'JANUARY':
        monthnum = 1
    elif month_name == 'FEBRUARY': 
        monthnum = 2
    elif month_name == 'MARCH':
        monthnum = 3
    elif month_name == 'APRIL':
        monthnum = 4
    elif month_name == 'MAY':
        monthnum = 5
    elif month_name == 'JUNE':
        monthnum = 6
    elif month_name == 'JULY':
        monthnum = 7
    elif month_name == 'AUGUST':
        monthnum = 8
    elif month_name == 'SEPTEMBER':
        monthnum = 9    
    elif month_name == 'OCTOBER':
        monthnum = 10
    elif month_name == 'NOVEMBER':
        monthnum = 11
    elif month_name == "DECEMBER":
        monthnum = 12    
    return monthnum 

def num_days_in(month_num, year):
    if is_leap.Boo == True and month_num == 2:
        daysin = 29 
    elif is_leap.Boo == False and month_num == 2:
        daysin = 28
    elif month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
        daysin = 30
    else:
        daysin = 31
    return daysin


def num_weeks(month_num, year):
    # Your code here
    startday = day_of_week(1, month_num, year)        #when the first is located on
    Tdays = num_days_in(month_num, year)         #Number of days in the month
    counter = 0                        # Value will change in loop for number of weeks
    
    for i in range(1, Tdays+1):
        if int(Tdays)%7 == 7:
            print()
        counter += 1
    
    return counter

def week(week_num, start_day, days_in_month):
    # Your code here
    noclue = 3

def main():
    month = input("Enter month:\n")
    year = input("Enter year:\n")


if __name__=='__main__':
    main()






