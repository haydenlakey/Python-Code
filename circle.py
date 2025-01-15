#Find area of circle, using esitmate of pi and radius
#Hayden Lakey
#LKYHAY001
#25 February 2022

import math
pi =  2 * 2/math.sqrt(2) * 2/math.sqrt(2+math.sqrt(2)) * 2/math.sqrt(2+math.sqrt(2+math.sqrt(2)))  

print("Approximation of pi:", round(pi, 4))

ask = eval(input("Enter the radius:\n"))
Area = pi * ask**2 
FArea = round(Area, 4)

print("Area:",FArea)
           