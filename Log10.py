#Log10 to find number of digits
#Hayden Lakey
#03 March 2022

num = eval(input("Enter Number: "))

digits = 0

while num > 0:
    digits = digits + 1
    num = num//10
print(digits)
     