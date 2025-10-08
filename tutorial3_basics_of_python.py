# Tutorial 5 - Python Number Methods

# -------------------- abs() --------------------
# abs(x) returns the absolute value of a number x

print(abs(10))       # 10
print(abs(-20))      # 20
print(abs(34.20))    # 34.2
print(abs(-55.02))   # 55.02


# -------------------- ceil() --------------------
# ceil(x) returns the smallest integer greater than or equal to x
# Note: Requires math module
import math

print(math.ceil(43.67))  # 44
print(math.ceil(43.3))   # 44
print(math.ceil(42.1))   # 43
print(math.ceil(-44.5))  # -44


# -------------------- floor() --------------------
# floor(x) returns the largest integer less than or equal to x
print(math.floor(43.1))   # 43
print(math.floor(43.9))   # 43
print(math.floor(-56.9))  # -57


# -------------------- exp() --------------------
# exp(x) returns e**x (exponential of x)
print(math.exp(10))   # 22026.465794806718
print(math.exp(-7))   # 0.0009118819655545162


# -------------------- fabs() --------------------
# fabs(x) returns the absolute value as a float
print(math.fabs(10.53))  # 10.53
print(math.fabs(-10))    # 10.0


# -------------------- log() --------------------
# log(x) returns the natural logarithm (base e)
print(math.log(10))      # 2.302585092994046
print(math.log(65.5))    # 4.182050142641207

# log10(x) returns the base-10 logarithm
print(math.log10(40))    # 1.6020599913279623


# -------------------- max() --------------------
# max() returns the largest value
print(max(10, 12, 5, 76, 100))  # 100
print(max(-55, -44, -33))       # -33


# -------------------- min() --------------------
# min() returns the smallest value
print(min(0, 100, 4, 5, 6, 3))  # 0
print(min(-1, 0))               # -1


# -------------------- pow() --------------------
# pow(x, y) returns x raised to the power y
print(math.pow(20, 5))   # 3200000.0
print(math.pow(-5, -5))  # -0.00032


# -------------------- sqrt() --------------------
# sqrt(x) returns the square root of x
print(math.sqrt(16))   # 4.0
print(math.sqrt(9))    # 3.0
print(math.sqrt(101))  # 10.04987562112089


# -------------------- Trigonometric Functions --------------------
print(math.sin(0))     # 0.0
print(math.cos(90))    # -0.4480736161291701 (since 90 radians ≈ 5157 degrees)
print(math.cos(0))     # 1.0
print(math.tan(45))    # 1.6197751905438615
print(math.tan(90))    # -1.995200412208242


# -------------------- hypot() --------------------
# hypot(x, y) returns sqrt(x*x + y*y)
print(math.hypot(2, 3))  # 3.6055512754639896


# -------------------- Assignment --------------------
# Try implementing the following:

# 1. Use math.modf() to separate integer and fractional parts of a number
# Example:
print(math.modf(12.345))  # (0.345, 12.0)

# 2. Program to check prime numbers
num = 13
if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 3. Program to find max of 3 numbers
a, b, c = 10, 25, 15
print("Maximum of 3 numbers:", max(a, b, c))
