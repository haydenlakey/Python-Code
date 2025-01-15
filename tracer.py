#Tracer program
#Hayden Lakey
#LKYHAY001
#2 May 2022

def listToString(s):  #Converts an array to string value that can be read
    str1 = "" 
    for ele in s: 
        str1 += ele   
    return str1  #Returns array as string

try:
    print("***** Program Trace Utility *****")
    Pyfile = input("Enter the name of the program file: ") 
    
    counter = 0  #Counter
    arr = [] #Empty Array
    file = open(Pyfile, "r", encoding = 'utf-8')
    
    for line in file:
          # line = line.replace('\n','')
            arr.append(line)
    file.close()    
 
    arrS = listToString(arr)   #Fills array as string
    CopyarrS = arrS  #Keeps copy of arrS before its modified
    #for word in arrS: 
    for word in arrS:    #For loop to run through arrS
        for let in word:
            Findb = arrS.find('(') 
            Finddef = arrS.find('def')
            FindC = arrS.find(":") #Finds the first colon 
            if let == 'def':
                print('Here', let)
    
    #arrS = '""'+'"Debug"'+'""'+'\n'+arrS[:FindC+1] + '\n' +'    """' +"DEBUG"+'"""'+";print('"+arrS[Finddef+4:Findb]+"')"+arrS[FindC+1:]  
   # print(arrS)
    
except IOError as errno:  #Throws an exception if an error is found
    print("Error has been found")
    print(errno)