#Functions to produce hollow squares
#Hayden Lakey
#LKYHAY001
#31 March 2022

import math

#Prints a 5x5 square 
def print_square():
    topline =  '* * * * *'
    mid1 =  '*       *'
    mid2 =  '*       *'
    mid3 = '*       *'
    bottomline = '* * * * *'
    return topline+'\n'+mid1+'\n'+mid2+'\n'+mid3+'\n'+bottomline
    
#Prints rectangle box with user input
def print_rectangle(width, height):
    if width == 2 and height == 2:
        print('* *')  
        print('* *')
    else:
        for i in range(width): 
            topline = '* '*width
            bottomline = topline
            for e in range(height-2): #The height excludig top and bottom
                gap = width - 1
                Length = (('*'+" "*(width-2+gap)+'*')+'\n')  # Value of the centre of rectangle
                Length = Length*(height-2)
        print(topline) 
        print(Length, end='')
        print(bottomline)
 

def get_rectangle(width, height):         #Essentially same code as above 
    Length = ''                            # except returns instead of prints
    if width == 2 and height == 2:
        topline = '* *'
        Lenth = ''
        bottomline = '* *'
    else:
        for i in range(width): 
            topline = '* '*width
            
            bottomline = topline
            for e in range(height-2):
                    gap = width - 1
                    Length = (('*'+" "*(width-2+gap)+'*')+'\n')
                    Length = Length*(height-2)
    return topline+'\n'+Length+bottomline    
        
