



print("***** Program Trace Utility *****")
Pyfile = input("Enter the name of the program file: ") 

Pfile = open(Pyfile, 'r')
A = []
for line in Pfile:
    line = line.replace('\n','')
    A.append(line)
Pfile.close

for important in A:
    
    print('Hello'+important)

        