# Constant examples
print()
print(12345)
print()
print("Hello, world\n")

#Variables examples
cheese = "mozzerella"
meat = "pepperoni"
pizza_toppings = f"{cheese} & {meat}\n"

print("pizza_toppings\n")

# Operator examples
x = 1
x = x + 1 

print(x)
print()                                         

'---------------------Reserved Python Words-------------------------'
# Reserved Words = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'-------------------------------------------------------------------'

# Expression examples

print("Addition 3 + 3")
xx = 3
xx = xx + 3

print(xx)
print()

print("Multiplication 33 * 10")
yy = 33 * 10

print(yy)
print()

print("Division 330 / 2")
zz = yy / 2

print(zz)
print()

print("Remainder 23 % 2")
jj = 23
kk = jj % 2

print(kk)
print()

print("Power 4 to the power of 3")
print(4 ** 3)
print()

# Types

int_type = 2 + 2
str_type = "hello, " + "world!"

print("Addition")
print("2 + 2 = ",int_type)

print("Integer type")
print(type(int_type))
print()

print("Concatinate")
print(str_type)
print("String type")
print(type(str_type))
print()

# String Conversion

num = 123
num_str = str(num)

print(" Multi-cursor: The integer value is:", num)
print(" Multi-cursor: The string value is:", num_str)
print(" Multi-cursor: Type of integer value is:", type(num))
print(" Multi-cursor: Type of string value is:", type(num_str))
print()
                      
 # User Input

name = input("What's your name? ")
east_asian_age = int(input("What is your east asian age? "))
age = int((east_asian_age)) - 1

print(f"Welcome, {name}, you are {age} year(s) old!")
print()

# Conditional Exacution


x = 15

if x < 10:
    print("bigger")
if x > 2:
    print("smaller")

print("finish")

# Comparison Operators

x = 5

if x == 5:
    print("Equals 5")
if x > 4:
    print("Greater than 4")
if x >= 5:
    print("Greater than or equal to 5")
if x < 6: 
    print("Lesser than 6")
if x <= 5:
    print("Less than or equal to 5")
if x != 6:
    print("Not equal 6")

# Indentation

print("> iterate")
x = 5

if x > 2:
	print("Bigger than 2")
	print("Still bigger")
print("Done with 2")

for i in range(5):
	print(i)
	if i > 2:
		print("Bigger than 2")
	print("Done with i', i")
print("All done")
print()

#  Indentation w/checks

x = 11

if x < 2:
    print("smaller")
elif x < 10:
    print("Medium")
else:
    print("Large")
print("All done")

# No Else

x = 50

if x < 2:
    print("small")
elif x < 10:
    print("Medium")
print("All done")

# Fail Puzzle

x = 5

if x < 2:
    print("Below 2")
elif x < 20:
    print("Below 20")
elif x < 10:
    print("Below 10") #Fails
else:
    print("Something else")

# Try & Except

astr = "bob"

try: 
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr)

user_str = input("Enter a number: ")
try:
    int_val = int(user_str)
except:
    int_val = -1

if int_val > 0:
    print("Nice work")
else:
    print("Not a nnumber")