#Search for anagram in text file
#Hayden Lakey
#LKYHAY001
#29 April 2022

def equal(W1, W2): #Checks if inputs are anagrams using 'characters' function
    W1 = characters(W1)
    W2 = characters(W2)
    if W1 == W2:
        return True
    else:
        return False

def characters(string):  #Function to find number of occurences of letters in word
    dCHR = {}
    for i in string:
        if i in dCHR:
            dCHR[i] += 1
        else:
            dCHR[i] = 1
    return dCHR

O = []
A = []
try:
    filepath = open("EnglishWords.txt", "r", encoding = 'utf-8')
    print("***** Anagram Finder *****")
    Oword = input("Enter a word: ") #Original word
    Oword = Oword.lower()
   
    
    for files in filepath:
        with open("EnglishWords.txt", 'r') as f:
            for line in f: 
                if 'START' in line: #Skips all lines till START is found
                    for line in filepath:
                        line = line.replace('\n','')
                        O.append(line)
                    for word in O:  #For every line in list starting from "START"  
                        if len(word) == len(Oword) and equal(Oword, word) == True: #Finds words with same length as input from user
                                A.append(word) 
                                if word == Oword:   
                                    A.remove(word) 
                              
    if A == []: #If array returned is empty then return the following
        print('')
        print("Sorry, anagrams of '"+Oword+ "' could not be found.") 
   
    else:
        print('')
        print(A) 
         
    filepath.close()
    
except EOFError as ef:
    print("***** Anagram Finder *****", ef)
    print("Sorry, could not find file 'EnglishWords.txt'.", ef)
    
except FileNotFoundError as Errno:  #If file is not found
    print("***** Anagram Finder *****")
    print("Sorry, could not find file 'EnglishWords.txt'.") 
    