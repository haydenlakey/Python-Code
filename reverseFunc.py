

def stringrev(a):
    reverse = ""
    for c in a:
        reverse = c + reverse 
    return reverse

orig = input("Enter sentence: ")

print(stringrev(orig))