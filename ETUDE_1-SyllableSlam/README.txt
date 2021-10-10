Etude 1 - Syllable Slam

Elsie Sun 4468203
Hugh McLeod-Jones 4668077
Ella Ji 2854080
James Pettitt 4713804

Langauge: Python

How to run main program:
 
Command line:

- change your working directory to where the python syllable files are saved. i.e ~/Desktop/etude 1

- To run the main program, type: python3 syllables.py
To run with our test file, type: python3 syllables.py < syllables_test.py

- You will then be presented with onscreen information to input any word, in which the syllable count is returned. This process will continue until you enter the text "exit program", at which instance the program terminates.

***********

To view test development:

- type: python3 test_development.py
- type: test()
- The output will show a list of the correct syllables our algorithm has predicted in comparison to a read text file of words with their accurate syllable count. wrong predictions will be shown, and over all accuracy will be presented out of 100% at the end.

Problem solution

We searched for syllable rules, and found a website that presents a solution for finding the number of syllables in a word using written rules. 

Source: https://medium.com/@mholtzscher/programmatically-counting-syllables-ca760435fab4 

General rules we attempted to cover in our code:

- Count the number of vowels (A, E, I, O, U) in the word.
- Add 1 every time the letter ‘y’ makes the sound of a vowel (A, E, I, O, U).
- Subtract 1 for each silent vowel (like the silent ‘e’ at the end of a word).
- Subtract 1 for each diphthong or triphthong in the word.
- Does the word end with “le” or “les?” Add 1 only if the letter before the “le” is a consonant.

The number you get is the number of syllables in your word.

Group Work

In terms of group work, we all developed a basic python script that attempted to implement our outlined rules. From there we commend the best ad hoc rules from each persons approach to come up with what we thought was the most accurate syllable detection algorithm.

We have used a method a file called test_development.py, which we used for development purposes as it allowed to compare a list of words with their Syllable count to the syllable output our algorithm produced, this way we could make incremental changes.


We have included a file called dictionary.txt, which contains over 16,000 words and there matching syllable counts, when running our test, we managed to get over 85% correct. The file dictionary.txt was sourced from another group in cosc326