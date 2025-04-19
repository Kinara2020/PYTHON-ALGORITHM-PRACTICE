# 1 Count uppercase and lowercase letters in a string
def count_lower_upper(text):
    result = {'uppercase': 0, 'lowercase': 0}
    for char in text:
        if char.isupper():
            result['uppercase'] += 1
        elif char.islower():
            result['lowercase'] += 1
    return result

print(count_lower_upper("Hello World!"))


# 2 Compute n + nn + nnn + nnnn
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")


# 3 Create a 3D Array
def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

print(create_array(2,2,2,5))


# 4 Calculate sum & average of 5 marks
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

print(sum_avg([80, 90, 70, 60, 85]))


# 5 Check if String is Pangram
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))


# 6 Create List of Tuples (x, x², x³)
def generate_tuples(start, end):
    return [(x, x**2, x**3) for x in range(start, end + 1)]

print(generate_tuples(1,5))


# 7 Check if String is Palindrome
def is_palindrome(s):
    clean = s.replace(" ", "").lower()
    return clean == clean[::-1]

print(is_palindrome("Madam In Eden Im Adam"))


# 8 Remove Duplicates and Sort Words
def count_alpha_digits(text):
    alpha_count = 0
    digit_count = 0
    
    for char in text:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1

    return {"Alphabets": alpha_count, "Digits": digit_count}


# 9 Count Alphabets and Digits
def count_alpha_digits(text):
    alpha_count = 0
    digit_count = 0
    
    for char in text:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1

    return {"Alphabets": alpha_count, "Digits": digit_count}


#10 Frequency of Words
def frequency_count(text):
    words = text.split()
    freq = {word: words.count(word) for word in set(words)}
    return dict(sorted(freq.items()))

print(frequency_count("apple banana apple orange banana apple"))


# 11 Intersection of Two Lists
def create_list(list1, list2):
    return list(set(list1) & set(list2))

common_list=create_list([1, 2, 3, 4], [3, 4, 5, 6])
print(common_list)

# 12 Recursive Prime Factors
def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n // i, i)
    return prime_factors(n, i + 1)

print("Prime Factors of 30:", prime_factors(30))


# 13 Convert Decimal to Binary (Recursive)
def decimal_to_binary(n):
    if n == 0:
        return ''
    return decimal_to_binary(n // 2) + str(n % 2)

num = 13
print(f"Binary of {num} is: {decimal_to_binary(num) or '0'}")


# 14 Count Vowels in String (Recursive)
def count_vowels(s):
    if not s:
        return 0
    return (s[0].lower() in 'aeiou') + count_vowels(s[1:])

print("Vowel count:", count_vowels("Pandit Deendayal Energy University"))


#15 Reverse List using Recursion
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

print("Reversed List:", reverse_list([1,2,3,4,5]))


# 16 Recursive Power Calculation (a^b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("2^5 =", power(2, 5))


# 17 Sanitize List (replace negatives with 0)
def sanitize_list(lst):
    if not lst:
        return []
    first = 0 if lst[0] < 0 else lst[0]
    return [first] + sanitize_list(lst[1:])

print("Sanitized List:", sanitize_list([3, -5, 7, -2, 9]))


# 18 Recursive Average Calculation
def recursive_average(lst):
    def helper(lst, count):
        if not lst:
            return 0
        return (lst[0] + helper(lst[1:], count)) if count > 0 else 0
    total = helper(lst, len(lst))
    return total / len(lst) if lst else 0

print("Average:", recursive_average([10, 20, 30, 40, 50]))


#19 Recursive String Length
def string_length(s):
    if s == '':
        return 0
    return 1 + string_length(s[1:])

print("Length of 'Python':", string_length("Python"))

