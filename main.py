#refactoring means to restructire code without changing its external behavior this helps improve code readability and maintainability.              
#importing the function from problem_set1.py
from problem_set1 import problem_1
from advance_slicing import advanced_slicing
#call the functionc
problem_1() # this is 
# an abstraction of function

# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
# b. Retrieve the second to last character.
# c. Find the first occurrence of the letter 'c'.

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
# b. Extract every second letter starting from 'a' to 'm'.
# c. Reverse the entire string using slicing.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
kanye = alphabet[7:10]
print(kanye)
hij_index = alphabet.index('hij')
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
# b. Extract every third word.
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Python is fun. Fun is good. Good is subjective."
print(info.rfind('subjective'))
subjective_word = info[info.rfind('subjective'):]
every_third_word = info.split()[::3]
reversed_words = ' '.join(reversed(every_third_word))
print(reversed_words)


# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
# b. Now, split the string at every occurrence of the letter 'a'.
text = "MAY THE FORCE BE WITH YOU."
lower_text = text.lower
print(lower_text())
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.

# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word
phrase = "Supercalifragilisticexpialidocious"
length_of_phrase = len(phrase)
count_of_i = phrase.count('i')
print(count_of_i)