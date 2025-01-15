#Weather stations
#Hayden Lakey 
#LKYHAY001
#31 March 2022
import math
def location(block):
    # Your code here   
    stringEnd = block.find("END")        #Finds word END
    stringO = block.find(" ",6,28)      # finds seond space
    Original = block[stringO + 1: stringEnd - 1]  
    Reverse = Original[::-1]   #Reverses extrscted string
    Reverse = Reverse.title()  #Makes first letter of each word capital
    return Reverse


def temperature(block): 
    # finds first soace and dash, then returns value between and rounds it
    findspace = block.find(' ')
    findd = block.find('_')
    temp = block[findspace+1:findd]
    temp = round(float(temp), 2)
    return temp

def x_coordinate(block):
    # Finds colon and and comma, returns value between them which is the coordinate
    findcolon = block.find(':')
    findcomma = block.find(',')
    xCord = block[findcolon+1:findcomma]
    return xCord

def y_coordinate(block):
    # finds comma and space and returns value between them
    findspace = block.find(' ')
    findcomma = block.find(',')
    findspace2 = block.find(' ', findspace+1)
    yCord = block[findcomma+1:findspace2]
    return yCord

def pressure(block):  
    # Finds lower dash and colon and returns value between them
    findP = block.find(':')
    findd = block.find('_')
    pressurevalue = block[findd+1:findP]    
    pressurevalue = math.floor(eval(pressurevalue))
    return pressurevalue

def get_block(data):
    # Gets string betwewn words BEGIN and END
    stringBegin = data.find("BEGIN")
    stringEND = data.find("END")
    stringvalue = data[stringBegin:stringEND+3]
    return stringvalue

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(float(temperature(block))))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
