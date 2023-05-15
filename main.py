#this is a commented line!

# Examples of Variables
name = "Michael" 
age = "33"
Birthday = "April 30"
__username__ = "Wilkode"

# Examples of Functions
print(name)
print(age)
print(type(__username__))
print(isinstance(name, str))
age = float(33)
print(isinstance(age, float))


# Mathematical inputs
1 + 1  # = 2 Addition
2 - 1  # = 1 Subtraction
2 * 2  # = 4 Multiplication
4 / 2  # = 2 Division
4 % 3  # = 1 Remainder 
4 ** 2 # = 16 Squared (Power of)
5 // 2 # = 2 (Floor division - Rounding down to the nearest number)

number = 8
number += 5 # age = age +8
number *= 5 # age = age *8

a = 1
b = 2
# Operators
a == b # False - Is exactly equal to
a != b # True - Is not equal to
a  > b # False - Is greater than
a <= b # False - Is less than or equal to

# Conditions// Boolean

condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 # False
condition1 or condition2 # True

# False will return the first value that is not false
# Or

print(0 or 1) # 1
print(False or 'hey') # 'hey'
print('hi' or 'hey') #  'hi'
print([] or False)   #False
print(False or [])   # []

# and - only moves onto the second statement if true

# & performs binary AND
# | performs binary OR
# ^ performs binary XOR
# ~ performs binary NOT
# << shift left operation
# >> shift right operation

# is - identity operator (used to compare 2x objects)
# in - membership operator (used to discover if value is in list/sequence)

def is_adult(age):
  if age > 18:
    return True
  else:
    return False

def is_adult2(age):
return True if age > 18 else False # Turnary operateor. If else


#Strings str

"Michael"
'Michael'
name = "Michael"
name += " is my name"   ## Michael is my name
print(name)            ## Michael is my name
phrase = "My name is" + "Michael"

age = str('33') #number is a string

#Multiline string

print("""Michael  

is 33

years old""")

# Michael  

# is 33

# years old

print("Michael".lower()) # all lower case
print("Michael".upper()) # all upper case
print("michael wilkinson".title()) # capitalised first letter for both!

isalpha() # check if a str contains characters or digits and is not empty
isdecimal() # check if a str contains digits and is not empty
lower() #to get a lowercase version of a string
islower() # check if a string contains lowercase letters
upper() # to get a uppercase version of a string
isupper() # check if a string contains uppercase letters
title() # to get a capatalized version of a string
startswith() # to check if the string starts with a specific substring
endswith() # to check if the strings ends with a specific substring
replace() # to replace part of a string
split() #to split the string on a specific character separator
strip() #to trim the whitespace from a string
join() # to append new letters to a string
find() # to find the position of a substring

# all return a new modified string!! Doesn't change original string

print(len(name)) # will print length of string name
print("ae" in name) #print part of a string
# name = "Mich\"ael" ## Backslash escapes next character (eg " quotation mark is a string)

## \n = new line
## \\ = \ - escapes the first backslash

name = Michael

print(name[1]) ## will print i. Counting index starts at 0
print(name[-1]) ## will print l. negative(-1) starts count at the end
print(name[0:3]) ## Mic (returns characters starting from beginning to the 3rd character. )

done =  True

if done:
  print("yes")
else:
  print("no")

## numbers are always true in boolean, except 0
## strings are false only when empty



