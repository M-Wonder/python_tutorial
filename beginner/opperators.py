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






