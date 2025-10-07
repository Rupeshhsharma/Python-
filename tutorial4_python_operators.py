# ============================================
# Tutorial 4 - Python Operators
# ============================================

# --------------------------------------------
# Python Operators
# --------------------------------------------
# * Logical
# * Equality
# * Comparison
# * Arithmetic


# ============================================
# 4.1.1 Logical Operators
# ============================================

# In python, the following keywords are used for boolean operations:
# not - unary negation
# and - conditional AND
# or  - conditional OR

# --------------------------------------------
# Examples:
# --------------------------------------------
print(type(False))          # bool
print(bool(1))              # True

a = True
b = False

print(True and False)       # False
print(True or False)        # True
print(not False)            # True

age = int(input("Enter the age: "))
if age < 18 or age >= 35:
    print("Successful execution")


# ============================================
# Equality Operators
# ============================================
# Operators:
# is       -> a is b (same object)
# is not   -> a is not b (different objects)
# ==       -> a == b (same value)
# !=       -> a != b (different values)

a = "Rupesh"
b = "Rupesh1"
print(a == b)               # False

age = int(input("Enter the age: "))
if age == 18:
    print("You are in the teenager age")

a = "Rupesh"
b = "Rupesh"
print(id(a))
print(id(b))
print(a is b)               # True

lst = [1, 2, 3]
lst1 = [1, 2, 3]
print(id(lst))
print(id(lst1))
print(lst is lst1)          # False
print(lst is not lst1)      # True
print("Rupesh" != "Rupesh1")  # True


# ============================================
# Comparison Operators
# ============================================
# <   less than
# <=  less than or equal to
# >   greater than
# >=  greater than or equal to

marks = float(input("Enter the marks: "))

if marks >= 35:
    print("Pass")
    if marks >= 50 and marks <= 70:
        print("First")
elif marks < 35:
    print("Fail")


# ============================================
# Arithmetic Operators
# ============================================
# +   addition
# -   subtraction
# *   multiplication
# /   true division
# //  integer division
# %   modulo

print(24 + 24)  # 48
print(48 - 24)  # 24
print(48 * 24)  # 1152
print(48 / 4)   # 12.0
print(48 // 5)  # 9
print(48 % 5)   # 3
