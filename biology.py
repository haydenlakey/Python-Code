#Taxonomic ranks
#Hayden Lakey
#LKYHAY001
#03 March 2022

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skeleton = input("The skeleton is (internal/external)?\n")

if skeleton == "internal": 
    fert = input("The fertilisation of eggs occurs (within the body/outside the body)?\n")
    if fert == "within the body":
        young = input("Young are produced by (waterproof eggs/live birth)?\n")
        if young == "waterproof eggs":
            skin = input("The skin is covered by (scales/feathers)?\n")
            if skin == "scales":
                ans = "Reptile"
            else:
                ans = "Bird"
        else:
            ans = "Mammal"
    else:
        water = input("It lives (in water/near water)?\n")
        if water == "in water":
            ans = "Fish"
        else:
            ans = "Amphibian"
else:
    ans = "Arthropod"
    
print("Type of animal:",ans)
    
                    
                
    