#Reorganised combine program
#Hayden Lakey'
#LKYHAY001
#1 April 2022


def get_integer(s):
    s = input("Enter n:\n")
    k = input("Enter k:\n")
    if calc_factorial(s) == s:
        n = eval(s)
        return n
    else:
        k = eval(k)
        return k
    

def calc_factorial(a):
    nfactorial = 1
    n = get_integer(n)
    for i in range (1, n+1):
        nfactorial *= i
    return nfactorial
        
def calc_factorial(q):
    global n
    n = get_integer("n")
    k = get_integer(k)
    nkfactorial = 1
    for i in range (1, n-k+1):
        nkfactorial *= i
    return nkfactorial
   # Nopermu = "Number of permutations: "
   # permu = nfactorial // nkfactorial
   # return str(Nopermu)+str(permu)