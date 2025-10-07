# ============================================
# Tutorial 3 - Python Control Flows
# ============================================

# --------------------------------------------
# if statement
# --------------------------------------------
val = input("Enter the number ")
value_float = float(val)
if value_float % 2 == 0:
    print("The number is even")

# --------------------------------------------
# Example: Boolean check
# --------------------------------------------
print(10 % 2 != 0)

# --------------------------------------------
# if-else statement
# --------------------------------------------
val = input("Enter the number ")
value_float = float(val)
if value_float % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# --------------------------------------------
# Age form - nested if-else condition
# --------------------------------------------
age = float(input("Enter the age: "))

if age < 18:
    print("Minor Age")
elif age >= 18 and age <= 45:
    print("Mid Age")
elif age > 45 and age <= 50:
    print("Senior Mid Age")
else:
    print("Senior Citizen")

# --------------------------------------------
# Nested if-else inside another condition
# --------------------------------------------
age = float(input("Enter the age: "))

if age < 18:
    print("Minor Age")
    if age < 15:
        print("You are in School")
    else:
        print("You are in College")
elif age >= 18 and age <= 45:
    print("Mid Age")
elif age > 45 and age <= 50:
    print("Senior Mid Age")
else:
    print("Senior Citizen")

# --------------------------------------------
# Loop statements - for loop
# --------------------------------------------
lst = [1, 2, 3, 4, 5, 6, 7]
for i in lst:
    print(i ** 2)

# --------------------------------------------
# Find the sum of all elements in a list
# --------------------------------------------
lst = [1, 2, 3, 4, 5, 6, 7]
sum1 = 0
for i in lst:
    sum1 = sum1 + i
print(sum1)

# --------------------------------------------
# Find the sum of even and odd numbers
# --------------------------------------------
lst = [1, 2, 3, 4, 5, 6, 7]
even_sum = 0
odd_sum = 0

for i in lst:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print("Even sum is {}".format(even_sum))
print("Odd sum is {}".format(odd_sum))

# --------------------------------------------
# While loop example
# --------------------------------------------
i = 0
even_sum = 0
odd_sum = 0
while i <= 10:
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
    i = i + 1
print(even_sum, odd_sum)

# --------------------------------------------
# break statement example
# --------------------------------------------
x = 1
while x < 7:
    if x == 4:
        break
    print(x)
    x = x + 1

# --------------------------------------------
# continue statement example
# --------------------------------------------
x = 0
while x < 7:
    x = x + 1
    if x == 4:
        continue
    print(x)
