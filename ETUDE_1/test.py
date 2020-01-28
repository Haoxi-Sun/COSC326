# Method which returns the number of syllables in a word
def count_syllables(line):
    vowelCount = 0
    vowels = 'aeiouy' #we included y as a vowel as it was a common case for making a syllable. There are some exceptions however, that we create rules for below.
    
    #strips, makes the word lowercase, and removes any digits in the word
    wordUnFormatted = line.lower().strip().replace(" ", "")
    word = ''.join([i for i in wordUnFormatted if not i.isdigit()])

    # Underneath are some rules we found for finding the syllables
    # We undertook the method of counting all vowles in a word, then subtracting or adding this number based on exceptions below.

    if len(word) == 3:
        if word[0] in vowels and word[1] not in vowels and word[2] in vowels and word[-1] !="e":
               vowelCount = 2
        else: vowelCount = 1
        
    else:

        if len(word) == 1 and line[0] not in vowels:
            vowelCount = 1
            
        for char in word:
            if char in vowels:
                vowelCount += 1

        #dipthong
        a = 0
        b = 2
        while b <= len(word):
            dip = word[a:b]
            if dip[0] in vowels and dip[1] in vowels and dip not in "ia":
                vowelCount -= 1
            a+= 1
            b+= 1

        if word.endswith("ie"):
            vowelCount += 1
                    
        if word.endswith('e'):
            vowelCount -= 1
    
            
        if word.endswith('ed') and word[-3] != 't' and word[-3] not in vowels:
            vowelCount -= 1

        if word.endswith('le') and len(word) > 2 and word[-3] not in vowels :
            vowelCount += 1

        if word.endswith('les') and word[-4] not in vowels:
            vowelCount += 1

        if len(word) > 0 and vowelCount == 0:
            vowelCount += 1
        
        

        #REMOVED THIS CODE BECAUSE IT BROKE IT FOR WORDS LIKE 'BEAUTY'
        #triphthong
        a = 0
        b = 3
        while b < len(line):
            trip = line[a:b]
            if trip[0] in vowels and trip[1] == 'y'and trip[2] in vowels:
                vowelCount += 1
            #if trip[0] in vowels and trip[1] in silentConsonants and trip[2] in vowels:
#                vowelCount -= 1
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
                    #print(len(line))
                    #print(trip[3])
                    vowelCount -= 1
                a += 1
                b += 1
        
    return vowelCount

#method used for comparing our output from syllablec_count method with
def test():
    test_syllables = open("syllable_list.txt", "r")
    line = test_syllables.readline().strip()

    #accuracy variables
    total_number_words = 0
    total_number_accurate = 0
    total_number_wrong = 0
    
    current_syllable_count = 0

    while line:
        x = line.split()
        if len(x) == 2 and x[1] == "Syllable":
            current_syllable_count = int(x[0])
            print(current_syllable_count)
            line = test_syllables.readline()

        else:
            total_number_words += 1
            our_syllable_count = count_syllables(line)
            if our_syllable_count != current_syllable_count:
                #print("Our output was" + our_syllable_count + "right output was" + current_syllable_count)
                print("Our output for {} was {} , the right output for {} was {}".format(line, our_syllable_count, line, current_syllable_count))
                total_number_wrong += 1
            else:
                print("Correct")
                total_number_accurate += 1
            line = test_syllables.readline().strip()
       

    #print("accuracy in %: " + (total_number_accurate/total_number_words)*100)
    print("Accuracy in % was {}".format((total_number_accurate/total_number_words)*100))
    test_syllables.close()

#method used for comparing our output from syllablec_count method with an external file with 16,000 words and assosiated syllable count
def test2():
    test_syllables = open("dictionary.txt", "r")
    line = test_syllables.readline().strip()

    #accuracy variables
    total_number_words = 0
    total_number_accurate = 0
    total_number_wrong = 0
    current_syllable_count = 0
 
    while line:
        
        x = line.split()
        total_number_words += 1
        our_syllable_count = count_syllables(x[0])
        
        if our_syllable_count != int(x[1]):
            total_number_wrong += 1
        else:
            total_number_accurate += 1
            
        line = test_syllables.readline().strip()
   
    print("Accuracy in % was {}".format((total_number_accurate/total_number_words)*100))
    test_syllables.close()

if __name__ == "__main__":
    test2()
