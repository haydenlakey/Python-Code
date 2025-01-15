#Checking if coordiantes are valid
#Hayden Lakey
#LKYHAY001
#03 March 2022

lat1 = eval(input("Enter first number:\n"))
lat2 = eval(input("Enter second number:\n"))
lat3 = eval(input("Enter third number:\n"))

long1 = eval(input("Enter fourth number:\n"))
long2 = eval(input("Enter fifth number:\n"))
long3 = eval(input("Enter sixth number:\n"))

if lat1 >= -90 and lat1 <= 90: 
    if long1 >= -180 and long1 <= 180:
        if lat2 >= 0 and lat2<= 59:
            if long2 >= 0 and long2<= 59:
                if lat3 >= 0 and lat3<= 59:
                    if long3 >= 0 and long3<= 59:
                        print("WOW! Looks like geographic coordinates!")
                    else:
                        print("Hmmm ... looks like 6 random numbers.")
                else:
                    print("Hmmm ... looks like 6 random numbers.")
            else:
                print("Hmmm ... looks like 6 random numbers.")
        else:
            print("Hmmm ... looks like 6 random numbers.")
    else:
        print("Hmmm ... looks like 6 random numbers.")
else:
    print("Hmmm ... looks like 6 random numbers.")
            