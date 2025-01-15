#Bulletin Board
#Hayden Lakey'
#LKYHAY001
#13 March 2022

select = None 
message = None

while select!="X" and select!="x": 
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message") 
    print("(V)iew message") 
    print("(L)ist files") 
    print("(D)isplay file") 
    print("e(X)it")

    select = input("Enter your selection:\n")
    select = select
    if select == "E" or select =="e":
        message = input("Enter the message:\n")
    elif select == "V" or select == "v" and message!=None :
        print("The message is:", str(message))
    elif select == "V"or select == "v" and message == None:
        print("The message is: no message yet")
    elif select == "L" or select == "l": 
        print("List of files: 42.txt, 1015.txt")
    elif select == "D" or select == "d":
        filen = input("Enter the filename:\n")
        if filen == "42.txt":
            print("The meaning of life is blah blah blah ...")
        elif filen == "1015.txt":
            print("Computer Science class notes ... simplified")
            print("Do all work")
            print("Pass course")
            print("Be happy")
        else:
            print("File not found")
                  
else:
    print("Goodbye!")
    
