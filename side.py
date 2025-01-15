#Calculate length of side and validate user input
#Hayden Lakey
#LKYHAY001
#27 February 2022

import math
sidea = eval(input("Enter the length of side a:\n")) 
sidec = eval(input("Enter the length of side c:\n"))

if sidea > 0 and sidec > 0:
        sideb = math.sqrt(sidec**2 - sidea**2)
        print("The length of side b is",sideb, end=".")
else:
        print("Sorry, lengths must be positive numbers.")
   
    