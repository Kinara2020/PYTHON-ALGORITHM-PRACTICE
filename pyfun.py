#question1
def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

# Store functions in a list
functions = [fun, disp, msg]

# Call each function in a loop
for f in functions:
    f()


#question2
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

# Add corresponding elements
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum of corresponding elements:", result)


#question3
import random

# Generate random numbers between -15 and 15
random_numbers = [random.randint(-15, 15) for _ in range(10)]
print("Original list:", random_numbers)

# Create new list with squares
squared_numbers = list(map(lambda x: x ** 2, random_numbers))
print("Squared list:", squared_numbers)


#question4
lst = ['madam', 'Python', 'malayalam', 12321]

# Convert all elements to string, then check palindrome
palindromes = list(filter(lambda s: str(s) == str(s)[::-1], lst))

print("Palindromes in the list:", palindromes)


#question5
faculty_names = ["CHINTANSIR", "NITINSIR","ANSARISIR", "SHIVRAMSIR", "VIRAJMAM"]

# Filter names longer than 8 characters
long_names = list(filter(lambda name: len(name) > 8, faculty_names))

print("Names longer than 8 characters:", long_names)



