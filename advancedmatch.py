#Wildcard strings
#Hayden Lakey
#LKYHAY001
#26 April 2022

def match(pattern, word):
    findA = pattern.find("*")
    Lword = len(word) 
    rest = pattern[findA+1:]  #Finds rest of word after *
    Lrest = len(rest)
    findrest = word.find(rest)
    if pattern == "q":
        return ""
    elif Lword - Lrest == Lword: #If the remainder does not change
        if pattern[:findA] == word[:findA]: 
            ans = "It's a match."
        elif pattern[:findA] != word[:findA]:
            ans = "They don't match."
        return ans
    elif word[findA] != "*" and word[Lword-Lrest:] == pattern[findA+1:]: #checks the end of begining of sentences are same
        ans = "It's a match." # ie only the middle has been changed, if not returns not same
        return ans
   
    elif pattern[0] == "?" and pattern[1:]==word[1:]:
        ans = "It's a match."
        return ans
    elif pattern[0]==word[0]:
        if len(pattern) == len(word):
            findq = pattern.find("?")
            if word[findq] != "?":
                ans = "It's a match."
            else:
                ans = "They don't match."
        else:
            ans = "They don't match."
        return ans
    else:
        ans = "They don't match." 
        return ans
 
p = input("Enter a pattern (or 'q' to quit):\n")
w = input("Enter a word:\n")
print(match(p, w))