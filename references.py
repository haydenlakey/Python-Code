#convert references
#Hayden Lakey 
#LKYHAY001
#19 March 2022
 
ref = input("Enter the reference:\n")
nref = len(ref)
start = 0 

com = ref.find(",") 
comma1 = ref[com+2].capitalize()
ref = ref.replace(ref[com+2], comma1, 1)
 
ref1 = ref[0].capitalize()                   #capitalize first letter
ref = ref.replace(ref[0],ref1, 1) 
 
brac = ref.find(")")
bracketC = ref[brac+2].capitalize() 
com3 = ref.find(",",brac,nref)                 
lowerbrac = ref[brac:com3].lower()
ref = ref.replace(ref[brac:com3], lowerbrac,1)   #makes everything lowercase from bracket to second comma
ref = ref. replace(ref[brac+2], bracketC,1)         # makes lettter after bracket capital

lower1 = ref[1:com].lower()
ref = ref.replace(ref[1:com],lower1)

bracket = ref.find("(")
title1 = ref[com:bracket].title()
ref = ref.replace(ref[com:bracket], title1)

print("Reformatted reference:")
print(ref)