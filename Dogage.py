#Converting humans and dogs age
#Hayden Lakey
#18 February 2022

Adog = eval(input("Insert dog's age: "))

if (Adog<=2):
    Ans = Adog*10.5
    
elif(Adog>2):
    Ans1 = Adog-2
    Ans2 = Ans1 * 4 
    Ans = Ans2 + 21
    
print("Dog is ",Ans," years old, in human years")
    

 