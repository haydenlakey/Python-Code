#Checking the validity of time from user input
#Hayden Lakey
#LKYHAY001
#27 February 2022

ihours = eval(input("Enter the hours:\n"))
imin = eval(input("Enter the minutes:\n"))
isec = eval(input("Enter the seconds:\n"))
 
if ihours >= 0 and ihours <= 23: 
    ans = "valid" 
    if imin >= 0 and imin <= 59:
        ans = "valid"
        if isec >= 0 and isec <= 59: 
            ans= "valid" 
        else:
            ans = "invalid"
    else:
        ans = "invalid"
else:
    ans = "invalid"
    
print("Your time is",ans,end=".")