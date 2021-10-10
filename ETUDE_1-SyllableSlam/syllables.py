# using the 'written method' rules of syllable counting:

# count all the vowels in the word however:
# we are assuming each 'y' makes the sound of a vowel
# subtract 1 for each silent vowel
# subtract 1 for each dipthong/tripthong
# if the word ends in 'le(s)', add 1 ONLY if the previous letter is a consonant



import fileinput
import sys

vowels = 'aeiouy' #we included y as a vowel as it was a common case for making a syllable. There are some exceptions however, that we create rules for below.
vowelCount = 0

#to make sure the stdin is word not integer and at which instance the program terminates
for line in sys.stdin:

    line = line.strip()

    """if(line == "exit program"):
        sys.exit(1)"""
  
    if(line.isalpha() == False):
        print("don't use numbers")
        continue
    
    #the vowel count equal to 0 at the beginning
    vowelCount = 0

    #strips, makes the word lowercase, and removes any digits in the word
    wordUnFormatted = line.lower().strip().replace(" ", "")
    word = ''.join([i for i in wordUnFormatted if not i.isdigit()])

    # Underneath are some rules we found for finding the syllables
    # We undertook the method of counting all vowles in a word, then subtracting or adding this number based on exceptions below.
    
    if len(word) == 3:
        #if a word consists of only three letters, the first and the last are both vowels and the middle is a consonant
        #also the last letter is not 'e', vowel count equal to 2, otherwise vowel count equal to 1
       if word[0] in vowels and word[1] not in vowels and word[2] in vowels and word[-1] !="e":
              vowelCount = 2
       else: vowelCount = 1
        
    else:
        #count single letter
        if len(word) == 1 and line[0] not in vowels:
            vowelCount = 1
        #if there are vowels in word, vowel count plus 1    
        for char in word:
            if char in vowels:
                vowelCount += 1

        #diphthong
        #if it is a diphthong, subtract one from the vowel count
        #scans through the word, checking each pair and if it is a dipthong
        a = 0
        b = 2
        while b <= len(word):
            dip = word[a:b]
            if dip[0] in vowels and dip[1] in vowels and dip not in "ia":
                vowelCount -= 1
            a+= 1
            b+= 1
        # if dipthongs are on the end of the word, and the e is the last word, add one to vowel count to avoid double depletion
        if word.endswith("ie"):
            vowelCount += 1
        
        #if the word end with 'e', the vowel count will minus one    
        #word like 'home'        
        if word.endswith('e'):
            vowelCount -= 1
        
        #if the word end with 'ed' and the third letter from the end of the word is not 't', vowel count minus one    
        #word like 'used'
        if word.endswith('ed') and word[-3] != 't' and word[-3] not in vowels:
            vowelCount -= 1
        #if word end with 'le', the length of the word bigger than 2 and also the third letter from the end of the word is not in the vowels
        #vowel count plus one
        #word like 'able'
        if word.endswith('le') and len(word) > 2 and word[-3] not in vowels :
            vowelCount += 1
        #if the word end with 'les' and the forth letter from the end of the word is not in vowels, vowel count plus one
        #word like 'ankles'
        if word.endswith('les') and word[-4] not in vowels:
            vowelCount += 1
        #if the length of the word greater than 0 and vowel count equal to 0, vowel count plus one
        if len(word) > 0 and vowelCount == 0:
            vowelCount += 1

        #triphthong
        #scans through the word, checking each pair and if it is a dipthong
        a = 0
        b = 3
        while b < len(line):
            trip = line[a:b]
            if trip[0] in vowels and trip[1] == 'y'and trip[2] in vowels:
                vowelCount += 1
            a += 1
            b += 1

        # Finds silent e's in a word that are not at the end of a word
        # if an e is proceded by a 'u' or 'o' then an constant, then followed by another constanat, it appears to be silent.
        if len(word) > 4:
            
            a = 0
            b = 4
            while b < len(line):
                trip = line[a:b]
                if trip[0] in "ou" and trip[1] not in vowels and trip[2] == 'e' and trip[3] not in "r":
                    vowelCount -= 1
                a += 1
                b += 1
        
    #print out how many syllables are there in a word
    if(vowelCount > 0):    
        syllableCount = vowelCount
        print("Syllables in '{}': {}".format(word, syllableCount))
    else: print("Please enter a word " + str(vowelCount))
