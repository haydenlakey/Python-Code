#Producing sequence of 10 numbers
#Hayden Lakey
#LKYHAY001
#03 March 2022

ask = eval(input("Enter the start number:\n"))

if ask > -6 and ask < 93:
    for out in range(ask, ask+7):
        ask ="{0:2}".format(out)    
        print(ask, end=' ')
        
else:
    print("ERROR! Please enter valid input")