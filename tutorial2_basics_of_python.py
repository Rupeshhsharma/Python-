# ============================================
# Tutorial 2 - Basics of Python
# ============================================

# --------------------------------------------
# Printing output
# --------------------------------------------
print("Hello world")
print("Welcome To my channel")

# --------------------------------------------
# Single line and multi-line comments
# --------------------------------------------
'''
Welcome to my youtube
channel
'''
print("Hello")

# --------------------------------------------
# Variable declaration
# --------------------------------------------
a = 10
print(type(a))
print(a)

tenth = 10
b = 40
c = "Rupesh"
print(type(c))

a1 = 10
first_name = "Rupesh"
print(first_name)

# --------------------------------------------
# Integer operations
# --------------------------------------------
a = 10
print(type(a))
print(a + 10)
print(a * 10)
print(a / 10)
print(a % 10)
print(type(a))

a = 10
b = 20
print(a + b)

# --------------------------------------------
# Floating point
# --------------------------------------------
a = 190.5
print(a)
print(type(a))

# --------------------------------------------
# Typecasting
# --------------------------------------------
print(float(b))

# --------------------------------------------
# Boolean
# --------------------------------------------
a1 = True
b1 = False
print(type(a1))
print(a1 | b1)

# --------------------------------------------
# Strings
# --------------------------------------------
name1 = "Rupesh"
print(name1)
print(type(name1))
print(name1 + "Rupesh")
print(name1 + str(1))

# --------------------------------------------
# Complex numbers
# --------------------------------------------
j = 1.0 - 2.3j
print(j)
print(j.real, j.imag)

# --------------------------------------------
# Dynamic Typing
# --------------------------------------------
a = 10
a = "Rupesh"

# --------------------------------------------
# Strong Typing
# --------------------------------------------
a = "Rupesh"
print(a + str(1))

# --------------------------------------------
# String Formatting
# --------------------------------------------
a = 100
print("The values is - ", a)

first_name = "Rupesh"
last_name = "Sharma"
print("The first name is {a} and last name is {b}".format(b=last_name, a=first_name))

# --------------------------------------------
# Input example
# --------------------------------------------
a = input("Enter the number A ")
b = input("enter the number B ")
print(int(a) + int(b))
