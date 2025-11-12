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
#specific data type
str1=str("hello world")#string
int1=int(20)#integer
float1=float(20.5)#float
complex1=complex(1j)#complex
list1=list(("apple" "banana" "cherry"))#list
tuple1=tuple(("banana" "apple" "cherry"))#tupple
range1=range(6)#range
dict1=dict(name3="john", age2=36)#
frozenset1 = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
boolean1 = bool(5) 	#bool 	
bytes1 = bytes(5) 	#bytes 	
bytearray1 = bytearray(5) 	#bytearray 	
memoryview1 = memoryview(bytes(5))#memoryview

#Setting the Data Type
x2complex=1j
list2=["apple" "banan" "cherry"]
tuple2=("apple" "banana" "cherry")
dict2={"name":"john", "age":36 }
set2={"apple", "banana", "cherry"}
frozenset2=({"apple", "banana", "cherry"})
bool2=True
bytes2=b"apple"
bbytearray2=bytearray(6)
e = 1 ;print(type(e))   # int
f = 2.8 ;f2 = 35e3; print(type(f)) # float. Float can also be scientific numbers with an "e" to indicate the power of 10.; 
g = 1j; g2= 3+5j; print(type(g))   # complex. Complex numbers are written with a "j" as the imaginary part:

#type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 

#random number using in built random module
import random
print(random.randrange(1, 10))

#python casting
cast1 = int(1)   # x will be 1
float3= float("3")   # z will be 3.0
string3 = str(3.0)  # z will be '3.0'
print(cast1)
print(float3)
print(string3)

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("He is called 'Johnny'")

#You can assign a multiline string to a variable by using three quotes:
multstrng = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multstrng)

#Strings are Arrays
strays = "Hello, World!" #Get the character at position 1  first character has the position 0
print(strays[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for y in "banana":
  print(y) 

  #To get the length of a string, use the len() function.
len1 = "Hello, World!"
print(len(len1))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)
#Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
 print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#You can return a range of characters by using the slice syntax.
slcice2 = "Hello, World!"
print(slcice2[2:5])
#by leaving out the start index, the range will start at the first character:
slcice2 = "Hello, World!"
print(slcice2[:5]); print(slcice2[2:]) #By leaving out the end index, the range will go to the end:

#Use negative indexes to start the slice from the end of the string:
slcice2 = "Hello, World!"
print(slcice2[-5:-2])

#The replace() method replaces a string with another string
replace1= "Hello, World!"
print(replace1.replace("H", "J"))
#The split() method returns a list where the text between the specified separator becomes the list items.
split1 = "Hello, World!"
print(split1.split(",")) # returns ['Hello', ' World!'] 

#String Concatenation To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age5 = 36
txt = f"My name is John, I am {age5}"
print(txt)

#A placeholder can contain variables, operations, functions
price = 75
txt5 = f"The price is {price} dollars"
print(txt5)
#and modifiers to format the value.
#A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 75
txt5 = f"The price is {price:.3f} dollars"
print(txt5)

#A placeholder can contain Python code, like math operations:
txt = f"The price is {20 * 59} dollars"
print(txt)

#to insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
escape1 = "We are the so-called \"Vikings\" from the north."

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#carriage return
txt = "Hello\rWorld!"
print(txt) 

#new line\n
txt = "Hello\nWorld!"
print(txt) 

##This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#tab \t
txt = "Hello\tWorld!"
print(txt) 

#String Methods
#Python has a set of built-in methods that you can use on strings.
#Note: All string methods return new values. They do not change the original string.






 














