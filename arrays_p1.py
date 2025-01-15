#Hayden Lakey
#7 April 2022

arr = []
count = 0

while count <= 4:
    ask = input('Please insert string:\n')
    count += 1 
    arr.append(ask)
for i in range(len(arr)):
    print(i, arr[i])

    