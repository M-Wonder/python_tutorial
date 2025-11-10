name="Wonder"
print(name)
print(name.upper())


name2="rodger"; print(name2) #this is an inline comment
#this is a commented line
print(type(name2))
print("ger" in name)
print(isinstance(name, str))
print(len(name2))

#float
fraction=2.1
print(type(fraction ==float))

#class constructor
age= int("20"); print(age)

fraction1= 0.1; intFraction =int(fraction1)
print(intFraction)

#Operators in Python
#assignment, arithmetic, comparison, logical, bitwise and interseting ones like is and in
Age=8 # "=" assignment oprerator
Age += 10; print(Age)

#arithmetic
1 + 1; 2 - 1; 2 * 2; 4 / 2; 4 % 3; 4 ** 2; 4 // 2

concatenate= "rodger" + " is a good dog"; print(concatenate)

#comparison operators "==, !=, >, <, >=, <="
a=1; b=12; print(a==b); print(a !=b); print(a>b); print(a<=b)

#boolean operators "not", "and", "or"
#or used in an expression returns the value of the first operand that is not a falsy value (False, 0, '', []..). Otherwise it returns the last operand.
print(0 or 1) ## 1
print(False or 'hey') ## 'hey'
print('hi' or 'hey') ## 'hi'
print([] or False) ## 'False'
print(False or []) ## '[]'


#biwise operators Bitwise operators in Python

#Some operators are used to work on bits and binary numbers:
   # & performs binary AND
   # | performs binary OR
  #  ^ performs a binary XOR operation
   # ~ performs a binary NOT operation
   # << shift left operation
   # >> shift right operation

#is is called the identity operator. It is used to compare two objects and returns true if both are the same object. More on objects later.
#in is called the membership operator. Is used to tell if a value is contained in a list, or another sequence. More on lists and other sequences later.

#The Ternary Operator in Python
def is_adult(Age):
    if Age > 18:
        return True
    else:
        return False
    
def is_adult(Age):
    return True if Age >18 else False

print(is_adult(Age))

#booleans in python Python provides the bool type, which can have two values: True and False (capitalized).
 # numbers are always True except for the number 0
    #strings are False only when empty
    #lists, tuples, sets, and dictionaries are False only when empty
done = True
print(type(done) == bool )
print(isinstance(done, bool))


#numbers in python Numbers in Python can be of 3 types: int, float and complex.


