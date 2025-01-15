#Convert time stamps
#Hayden Lakey
#LKYHAY001
#18 March 2022

month = None
hour = None  
date = (input("Enter the date and time (yyyy-mm-dd hh:mm):\n"))
date = str(date)

if date[8:10] == "01" or date[8:10] == "21":
   suf = "st"
elif date[8:10] == "03" or date[8:10] == "23":
   suf = "rd"
elif date[8:10] == "02" or date[8:10] == "22":
   suf = "nd"
else:
   suf = "th"
   
if date[11:13]>="12" and date[11:13]<="23":
   merid = "pm"
else:
   merid = "am"
   
if date[5:7] == "01":
   month = "January"
elif date[5:7] == "02":
   month = "February"
elif date[5:7] == "03":
   month = "March"
elif date[5:7] == "04":
   month = "April"
elif date[5:7] == "05":
   month = "May"
elif date[5:7] == "06":
   month = "June"
elif date[5:7] == "07":
   month = "July"
elif date[5:7] == "08":
   month = "August"
elif date[5:7] == "09":
   month = "September"
elif date[5:7] == "10":
   month = "October"
elif date[5:7] == "11":
   month = "November"
elif date[5:7] == "12":
   month = "December"

if date[11:13] == "00" :
   hour = "12"
elif date[11:13] == "13" or date[11:13]=="01":
   hour = "1"
elif date[11:13] == "14" or date[11:13] == "02":
   hour = "2"
elif date[11:13] == "15" or date[11:13]== "03":
   hour = "3"
elif date[11:13] == "16" or date[11:13] == '04':
   hour = "4"
elif date[11:13] == "17" or date[11:13]== '05':
   hour = "5"
elif date[11:13] == "18" or date[11:13]=='06':
   hour = "6"
elif date[11:13] == "19" or date[11:13]=='07':
   hour = "7"
elif date[11:13] == "20" or date[11:13]=='08':
   hour = "8"
elif date[11:13] == "21" or date[11:13]=='09':
   hour = "9"
elif date[11:13] == "22" or date[11:13]=='10':
   hour = "10"
elif date[11:13] == "23" or date[11:13]=='11':
   hour = "11"
else:
   hour = date[11:13]

if date[8] == "0":  
   print(hour+date[13:16],end='') 
   print(" "+merid, "on the",date[9]+suf,"of",month,"'"+date[2:4])

else:
   print(hour+date[13:16],end='') 
   print(" "+merid, "on the",date[8:10]+suf,"of",month,"'"+date[2:4])   
   