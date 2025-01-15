#Find smallest number out of 4 numbers
#Hayden Lakey
#22 February 2022

inp1 = eval(input("Please insert number: "))
inp2 = eval(input("Please insert another number: "))
inp3 = eval(input("Please insert a third number: "))
inp4 = eval(input("Please insert one last number: "))

if(inp1< inp2) and (inp1<inp3) and (inp1<inp4):
    ans = inp1    

if(inp2< inp1) and (inp2<inp3) and (inp2<inp4):
    ans = inp2   
    
if(inp3< inp1) and (inp3<inp2) and (inp3<inp4): 
    ans = inp3    
   
if(inp4< inp1) and (inp4<inp2) and (inp4<inp3):
    ans = inp1    

print(ans)