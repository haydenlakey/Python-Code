#Print out calendar
#Hayden Lakey
#LKYHAY001
#10 March 2022

month = input("Enter the month ('January', ..., 'December'):\n")
day = input("Enter the start day ('Monday', ..., 'Sunday'):\n")

if month == "April": 
    nMonth = 30
elif month == "February": 
    nMonth = 28
elif month == "June": 
    nMonth = 30
elif month == "September":
    nMonth = 30 
elif month == "November":
    nMonth = 30
else:
    nMonth = 31

print(month)
print("Mo","Tu","We","Th","Fr","Sa","Su")

if day == "Monday" :
    print(end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==0):
            print()   
                
if day == "Tuesday" :
    print("   ",end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==6):
            print()
            
if day == "Wednesday"  :
    print("      ",end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==5):
            print()   

if day == "Thursday" :
    print("         ",end='')
    for date in range(1,nMonth+1): 
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==4):
            print()

if day == "Friday" :
    print("            ",end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==3):
            print()

if day == "Saturday" :
    print("               ",end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==2):
            print()
            
if day == "Sunday" : 
    print("                  ",end='')
    for date in range(1,nMonth+1):
        date = "{0:2}".format(date)
        print(date,'', end="")
        if (int(date)%7 ==1):
            print()