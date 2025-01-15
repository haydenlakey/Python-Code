#Ascii triangles with for loops
#Hayden Lakey
#02 March 2022

row = eval(input("how many rows "))
col = eval(input("how columns "))

for r in range(row): 
    for c in range(r+1):
        print("$", end='')
    print("") 