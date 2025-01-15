#Calculating a to the poer of b using for loop
#Hayden Lakey
#02 March 2022

anum = float(input("Enter base number: "))
bnum = int(input("Enter exponent number: "))

if bnum < 1:
    print("Must be positive value")
else:
    power = anum
    for ans in range(1, bnum):
        power*= anum 
    print(power)
    
    