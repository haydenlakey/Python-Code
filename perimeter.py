# A program to calculate the perimeter of a fence, and 
# its associated cost
# Name: Lebeko Poulo
# Student Number: PLXLEB003
# Date: 19 February 2022

# Obtain width 1 from the user
width_1 = eval(input("Enter width 1: \n"))

# obtain height 1 from the user
height_1 = eval(input("Enter height 1: \n"))

# Obtain width 2 from the user
width_2 = eval(input("Enter width 2: \n"))

#Obtain height 2 from the user
height_2 = eval(input("Enter height 2: \n"))

# Calculate the total distance around the fence - perimeter of the fence
perimeter = 2 * (width_1 + height_1 + width_2) 

# Print out the total fence required in meters, and
# The total price for the fence.
pricePerMetre = eval(input("Enter price per metre: \n"))
TotalPrice = pricePerMetre * perimeter 

print("The total required =", perimeter, "metres")
print("The total price = R", TotalPrice)
 