#Print out every 7th number
#Hayden Lakey
#LKYHAY001
#03 March 2022

ask = eval(input("Enter a number:\n"))

if ask > -6 and ask < 2:
    tots = ask + 41
    
    while ask < tots:
        ask = ask + 7 
        new = ask - 7  
        new = "{0:2}".format(new)
        print(new)

else:
    print("ERROR!")

   
      

        
    

