#Reverse of sentence string
#Hayden Lakey
#08 March 2022

strin = input("Please enter what you'd like reversed: ")


for pos in range(len(strin)-1, -1, -1):
    print(strin[pos], end = '') 