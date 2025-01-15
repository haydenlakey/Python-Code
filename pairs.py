#Counting pairs of letters
#Hayden Lakey
#LKYHAY001
#26 April 2022

def pairs(string):
    if string:              #Base case
        first, *secondc = string 
        if secondc:
            second, *thirdc = secondc
            if first == second:            #Recursive step
                return 1 + pairs(thirdc)
            return pairs(secondc)  
    return 0 

inp = input("Enter a message:\n")
print("Number of pairs:", pairs(inp))