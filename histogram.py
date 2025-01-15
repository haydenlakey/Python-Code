#create histogram for marks
#Hayden Lakey
#LKYHAY001
#21 April 2022
 
marks = input("Enter a space-separated list of marks:\n")
Amarks = []
Amarks.append(marks)
Dmarks = {'1': str(range(75, 101)), '2+':range(70, 75), '2-':range(60, 70),'3':range(50, 60),'F':range(0, 50)}
ans1=""
length = int(len(Amarks))

for length in Amarks:
    print(length)
  #  if Amarks[length]>= '75' and Amarks[length]<'101':
  #      ans1 +="X"

print("1 |" + ans1)   
print("2+|" )
print("2-|" )
print("3 |" )
print("F |" )
