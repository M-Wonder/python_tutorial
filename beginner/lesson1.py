name="Wonder"
print(name)
name2="rodger"; print(name2) #this is an inline comment
#this is a commented line
print(type(name2))
print(isinstance(name, str))

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
