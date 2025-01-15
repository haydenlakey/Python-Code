#Sketch functions
#Hayden Lakey
#LKYHAY001
#16 March 2022
 
#import math

function = input("Enter a function f(x):\n")
x = function.find('x')

for y in range(21):
    for x in range(21):
        if eval(function) == y:
            print('o')
        elif x==0 and y==0:
            print('+')
        elif x== 0 :
            print('|')
        elif y==0:
            print('-')
        else:
            print(' ')
        

        

    

    
