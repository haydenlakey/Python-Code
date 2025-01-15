# Order randomly arranged numbers
#Hayden Lakey
#23 February 2022

A1 = eval(input("Insert first number: "))
A2 = eval(input("Insert second number: "))
A3 = eval(input("Insert third number: "))

if A1<A2:
    if A1<A3:
        if A2 < A3:
            print(A1, A2, A3)
        else:
            print(A1, A3, A2)
    else: 
        print(A3, A1, A2)
else:
    if A2 < A3:
        if A1<A3:
            print(A2, A1, A3)
        else:
            print(A2, A3, A1)
    else:
        print(A3, A2, A1)

