#Gumatj number system functions
#Hayden Lakey
#LKYHAY001
#11 April 2022

def gumatj_to_decimal(a):
    
    if a < 5:    #Elif statements to supply values accordingly
        decimal = a
    elif a >= 10 and a<= 14:
        decimal = a - 5 
    elif a >= 20 and a < 30:
        decimal = a - 10
    elif a>= 30 and a < 40:
        decimal = a - 15
    elif a >= 40 and a < 44:
        decimal = a - 20
    return decimal 

def decimal_to_gumatj(a):
    
    if a < 5:            #Elif statements to supply values accordingly
        decimal = a
    elif a >= 5 and a <= 9:
        decimal = a + 5
    elif a >= 10 and a < 15:
        decimal = a + 10
    elif a>= 15 and a < 20:
        decimal = a + 15
    elif a >= 20 and a < 25:
        decimal = a + 20  
    return decimal

def gumatj_add(a, b): #Adds numbers as decimals, then converts decimal to gumatj
    return decimal_to_gumatj(gumatj_to_decimal(a) + gumatj_to_decimal(b))

def gumatj_multiply(a, b):#Adds numbers as decimals, then converts decimal to gumatj
    return decimal_to_gumatj(gumatj_to_decimal(a) * gumatj_to_decimal(b)) 