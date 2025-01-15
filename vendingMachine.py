#Vending machine and producing users change
#Hayden Lakey
#LKYHAY001
#11 March 2022

cost = eval(input("Enter the cost (in cents):\n"))

while cost > 0:
    deposit = eval(input("Deposit a coin or note (in cents):\n"))
    cost = cost - deposit

change = cost * -1

if change == 0:
    pass 

else: 
    R_5 = change // 500
    change = change%500
    R_2 = change // 200
    change = change %200
    R_1 = change // 100
    change = change%100
    c50 = change//50
    change = change%50 
    c20 = change//20
    change = change%20
    c10 = change//10
    change = change%10
    c5 = change//5
    
    
    print("Your change is:")
    
        
    if R_5 >0 :
        print(str(R_5)+ " x R5")
    if R_2 > 0:
        print(str(R_2 )+ " x R2")
    if R_1>0:
        print(str(R_1) + " x R1")
    if c50>0:
        print(str(c50)+ " x 50c")
    if c20>0:
        print(str(c20) + " x 20c")
    if c10>0:
        print(str(c10)+ " x 10c")
    if c5>0:
        print(str(c5)+ " x 5c")
        
