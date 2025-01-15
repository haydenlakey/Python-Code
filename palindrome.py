#Check if string is palindrome
#Hayden Lakey
#LKYHAY001
#26 April 2022

def reverse(string):
    if len(string) == 0: #If no input return
        return string
    else:
        return reverse(string[1:]) + string[0] #Reverses string recursivly

def palindrome(string):
    if string == reverse(string):   #Checks if string is the same as reverse
        yes = "Palindrome!"
        return yes
    else:
        no = "Not a palindrome!"   #If not the same returns different value
        return no

inp = input("Enter a string:\n")
print(palindrome(inp))       