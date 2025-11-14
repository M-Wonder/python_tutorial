#Python Assignment Operators
x = 5

x &= 3

print(x)

#It performs a bitwise OR between the bits of x and the bits of 3.|= is the bitwise OR assignment operator.
x = 5

x |= 3

print(x)

# ^= is the bitwise XOR assignment operator. XOR (exclusive OR) returns:
#1 if the bits are different
#0 if the bits are the same
x = 5
x ^= 3
print(x)

#>>= is the right-shift assignment operator. Shifting right removes bits from the right:
x = 5
x >>= 3
print(x)

#<<= is the left-shift assignment operator. Shifting left adds zeros on the right:
#Left shift moves the bits of the number to the left, and each shift multiplies the number by 2.
x = 5
x <<= 3
print(x)

#~ 	NOT 	Inverts all the bits 	~x
print(~3)

#:= is the walrus operator (introduced in Python 3.8).
print(x := 3); #same as
x = 3
print(3)

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")


#Python Comparison Operators
#Comparison operators return True or False based on the comparison:
x = 5
y = 3

print(x == y) #equal to
print(x != y) #not equal to
print(x > y) #greater than
print(x < y)# less than
print(x >= y)# greater than or equal to
print(x <= y)# less than or equal to 

#Python allows you to chain comparison operators:
x = 5
print(1 < x < 10)
print(1 < x and x < 10)

#Python Logical Operators
#and  	Returns True if both statements are true
#or 	Returns True if one of the statements is true
#not    Reverses the result, returns False if the result is true.

x = 5
print(not(x > 3 and x < 10)) #False
print(x>3 or x<4) #True

#Python Identity Operators
#is  	Returns True if both variables are the same object 	x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#is not 	Returns True if both variables are not the same object 	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content.


#Membership Operators. Membership operators are used to test if a sequence is presented in an object:
#in  	Returns True if a sequence with the specified value is present in the object 	x in y

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

#not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

#Python Operator Precedence







