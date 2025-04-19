# Question 1: Print all alphabets in upper case and lower case.
print("1 Alphabets in Uppercase and Lowercase:")
print("Uppercase Letters: ", end="")
for i in range(65, 91):
    print(chr(i), end=" ")
print("\nLowercase Letters: ", end="")
for i in range(97, 123):
    print(chr(i), end=" ")
print("\n" + "-"*50)

# Question 2: Print a multiplication table of a given number.
num = int(input("2 Enter a number to print its multiplication table: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("-"*50)

# Question 3: Count number of alphabets and number of digits in any given string.
input_string = input("3 Enter a string: ")
alpha_count = sum(char.isalpha() for char in input_string)
digit_count = sum(char.isdigit() for char in input_string)
print(f"Total Alphabets: {alpha_count}")
print(f"Total Digits: {digit_count}")
print("-"*50)

# Question 4: Check whether a given number is prime, perfect, Armstrong, palindrome, or automorphic.
number = int(input("4 Enter a number for various checks: "))

# Prime check
is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1)) if number > 1 else False

# Perfect number check
div_sum = sum(i for i in range(1, number) if number % i == 0)
is_perfect = div_sum == number

# Armstrong check
armstrong_sum = sum(int(digit) ** len(str(number)) for digit in str(number))
is_armstrong = armstrong_sum == number

# Palindrome check
is_palindrome = str(number) == str(number)[::-1]

# Automorphic check
square = number ** 2
is_automorphic = str(square).endswith(str(number))

# Display Results
print(f"Is {number} Prime? {'Yes' if is_prime else 'No'}")
print(f"Is {number} Perfect? {'Yes' if is_perfect else 'No'}")
print(f"Is {number} Armstrong? {'Yes' if is_armstrong else 'No'}")
print(f"Is {number} Palindrome? {'Yes' if is_palindrome else 'No'}")
print(f"Is {number} Automorphic? {'Yes' if is_automorphic else 'No'}")
print("-"*50)

# Question 5: Generate all Pythagorean Triplets with side length <= 30.
print("5 Pythagorean Triplets with side length ≤ 30:")
for a in range(1, 31):
    for b in range(a, 31):  # start from a to avoid duplicates
        c = (a**2 + b**2) ** 0.5
        if c == int(c) and c <= 30:
            print(f"Triplet: {a}, {b}, {int(c)}")
print("-"*50)

# Question 6: Print 24 hours of the day with suitable suffixes.
print("6 24 Hours of the Day with Suffixes:")
for hour in range(0, 24):
    if hour == 0:
        label = "Midnight"
    elif hour == 12:
        label = "Noon"
    elif hour < 12:
        label = f"{hour} AM"
    else:
        label = f"{hour - 12} PM"
    print(label)
print("-" * 50)

# Question 7: Print nCr and nPr.
import math
n = int(input("7 Enter value of n: "))
r = int(input("Enter value of r: "))
if r > n:
    print("Invalid input! r should not be greater than n.")
else:
    nCr = math.comb(n, r)
    nPr = math.perm(n, r)
    print(f"nCr (Combination) of {n} and {r} = {nCr}")
    print(f"nPr (Permutation) of {n} and {r} = {nPr}")
print("-" * 50)

# Question 8: Print factorial of a given number.
num = int(input("8 Enter a number to compute its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = math.factorial(num)
    print(f"The factorial of {num} is: {factorial}")
print("-" * 50)

# Question 9: Print N natural numbers in reverse.
N = int(input("9 Enter a number to print natural numbers in reverse: "))
if N < 1:
    print("Please enter a positive integer!")
else:
    print("Natural numbers in reverse:")
    for i in range(N, 0, -1):
        print(i, end=" ")
print("\n" + "-" * 50)

# Question 10: Generate N numbers of Fibonacci series.
count = int(input("10 Enter how many Fibonacci numbers you want: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(count):
    print(a, end=" ")
    a, b = b, a + b
print("\n" + "-" * 50)

# Question 11: Calculate sin(x) using series expansion.
x_deg = float(input("11 Enter angle in degrees to compute sin(x): "))
x = x_deg * (3.14159 / 180)  # Convert to radians
sin_x = 0
term = x
i = 1
sign = 1

# Using 7 terms for better accuracy
for n in range(1, 15, 2):
    term = sign * (x ** n) / math.factorial(n)
    sin_x += term
    sign *= -1  # Alternate the sign

print(f"Approximated sin({x_deg}°) is: {sin_x}")
import math as m
print(f"Built-in sin({x_deg}°) is: {m.sin(x)}")
print("-" * 50)
