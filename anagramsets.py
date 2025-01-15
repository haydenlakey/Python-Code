#Find anagram sets that have inputted length
#Hayden Lakey
#LKYHAY001
#3 May 2022
def groupAnagrams(words):
    """Stores and groups anagrams"""
    # a list to store anagrams
    anagrams = []
    if not words:
        return anagrams
 
    nums = [''.join(sorted(word)) for word in words]
    #Sorts words in for loop
    d = {}
    for i, e in enumerate(nums):
        d.setdefault(e, []).append(i) #Appends nagrams to set if they are actually anagrams of each other.(Groups anagrams)
 
    for index in d.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
    return anagrams

Originalarr = []
Samearr = [] 
anagram_list = []
print("***** Anagram Set Search *****")
Wlength = eval(input("Enter word length:\n"))
print("Searching...")
Fname = input("Enter file name:\n")
print("Writing results...")
 
filepath = open('EnglishWords.txt', 'r', encoding = 'utf-8')

for files in filepath:
    with open("EnglishWords.txt", 'r') as f:
        for line in f: 
            if 'START' in line:    
                for line in filepath: #New for loop to go through filepath
                    line = line.replace('\n','')
                    Originalarr.append(line) #Appends new inde to the array
                for word in Originalarr:  #For every line in list starting from "START"  
                    if len(word) == Wlength:   #Finds words with same length as input from user'
                        Samearr.append(word) 

Samearr.sort()                            
anagrams = groupAnagrams(Samearr)
external_file = open(Fname, 'w')                                                    
anagrams = sorted(anagrams)
for anagram in anagrams: 
    anagram = str(anagram)
    anagram =  anagram.replace('(','[') #Removes regular brackets for square brackets
    anagram =  anagram.replace(')',']')
    print(anagram)
    print(anagram, file=external_file)

print("^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^") 
print("|  |  |  |  |  |  |  |  |  |  |  |")
print("Program complete! View results above") 
                       
filepath.close()   
external_file.close() 