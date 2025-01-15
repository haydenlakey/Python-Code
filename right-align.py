#Align inputs from user to the right
#Hayden Lakey
#LKYHAY001
#19 April 2022

inputstring = input("Enter strings (end with DONE):\n")
array = [] #empty array

if inputstring == 'DONE':
    print('')
    print("Right-aligned list: ")
    print('')
else:   
    while inputstring != "DONE":
        array.append(str(inputstring)) #Adds new user input to array
        inputstring = input("") 
    
    longest = len(max(array, key = len)) #Finds length of longest word in array
    print('') 
    print("Right-aligned list: ")
    for i in array: 
        print(i.rjust(longest)) #right aligns to length of longest word