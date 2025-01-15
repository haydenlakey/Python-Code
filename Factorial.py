#Factorial of number user inputs
#Hayden Lakey
#02 March 2022

inp = eval(input("Enter factorial you desire: "))
inp = int(inp)
           
if inp>= 0:
    fact = 1
    for ans in range (1,inp+1):
        fact*=ans
    print(inp,"!=", fact)
else:
    print("not valid") 