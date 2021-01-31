# Password Generator
# Python 3.9.1
# Created by deathlezz
# Date 31.01.2021

import random

# A function do shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here

# Generate a random Uppercase letters (based on ASCII code)
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))

# Generate a random Lowercase letters (based on ASCII code)
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))

# Generate a random digit numbers (based on ASCII code)
digitNumber1 = chr(random.randint(48, 57))
digitNumber2 = chr(random.randint(48, 57))

# Generate a random punctuation signs (based on ASCII code)
sign1 = chr(random.randint(33, 38))
sign2 = chr(random.randint(33, 38))

# Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 \
           + lowercaseLetter1 + lowercaseLetter2 \
           + digitNumber1 + digitNumber2 \
           + sign1 + sign2

password = shuffle(password)

# Output
print(password)