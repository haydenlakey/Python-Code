#Palindrome Primes
#Hayden Lakey
#LKYHAY001
#27 April 2022 
import sys
sys.setrecursionlimit (30000)

def primes(N, M):
   N = int(N)
   M = int(M)
   a = []
   for number in range (N, M + 1):  
      if number > 1:  
         for i in range (2, number):  
            if (number % i) == 0:  
               break 
         else:     
            a.append(number)
   return a

def reverse_number(number, remain=0):
   number  = int(number)
   if number == 0:
      return (remain)//10
   else:
      return reverse_number(number//10, (remain+(number%10))*10)
  # rev = str(number)[::-1]
  # return rev

def Pprimes(N,M):
   N = int(N)
   M = int(M)
   A = []
   for i in range(N, M):
      i = str(i)
      R = i[::-1]
      array = primes(N, M)
      length = len(i)
      if i[0] == i[length-1]:
         if R in array:
            A.append(R)
         return A
         

 # A = str(('\n'.join(A)))
                  
start= input("Enter the starting point N:\n")
end = input("Enter the ending point M:\n")
print("The palindromic primes are:")
print(Pprimes(start,end))
