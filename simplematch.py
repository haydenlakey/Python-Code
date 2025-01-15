#Simple matching wildstring
#Hayden Lakey
#LKYHAY001
#26 April 2022  
 
def match(pattern, word):
    if pattern == "q":
        return ""
    elif pattern[0] == "?" and pattern[1:]==word[1:]: #If first letter is ? rest of word must match
        ans = "It's a match."
        return ans
    elif pattern[0]==word[0]:   #Checks first letter of each input 
        if len(pattern) == len(word):#Checks if words are same length
            findq = pattern.find("?") #Finds ? in pattern input
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