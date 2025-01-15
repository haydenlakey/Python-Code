#Convert from pig latin to english
#Hayden Lakey
#LKYHAY001
#12 April 2022

def to_pig_latin(sentence):
   sentence = sentence.lower()   #makes all letters lower case
   words = sentence.split()
   for i, word in enumerate(words):
      if word[0] in 'aeiou':       #Looks for vowel
         words[i] = words[i]+ "way"  #in the for loop adds way to the end
      else: 
         has_vowel = False 
         for j, letter in enumerate(word):
               if letter in 'aeiou':   #Searches for vowel in the whole length of each word
                  words[i] = word[j:] + "a" + word[:j] + "ay" #Rearranges the letters
                  has_vowel = True
                  break
         if(has_vowel == False):
            words[i] = words[i]+ "ay" #If no vowel found rearranges accordingly
      pig_latin = ' '.join(words)   
   return pig_latin       
            
def to_english(sentence):
   sentence = sentence.split(" ")  #Spaces between each word
   english = ""  #Empty string to start with
   for word in sentence:
      if word[:len(word) - 4:-1] == 'yaw': #Works backwards to find additinal text
            english += word[:len(word) - 3] + " "
      else: 
            noAY = word[:len(word) - 2] #
            firstconsonants = noAY.split("a")[-1] #Splits the word from a
            consonantsremoved = noAY[:len(noAY) - (len(firstconsonants)+1)]
            english += firstconsonants + consonantsremoved + " "
   return english