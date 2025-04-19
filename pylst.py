# Question 1: Count boys and girls in a list
print("1 Counting Boys (Tuples) and Girls (Strings) in a List:")
names = [('John',), 'Emily', ('Mike',), 'Anna', ('Chris',), 'Sophie']
boys = sum(1 for name in names if isinstance(name, tuple))
girls = sum(1 for name in names if not isinstance(name, tuple))
print(f"Total Boys: {boys}")
print(f"Total Girls: {girls}")
print("-" * 50)

# Question 2: Split list of tuples into separate lists
print("2 Splitting Tuple List into Separate Lists:")
students = [(101, "Alice", 20), (102, "Bob", 21), (103, "Charlie", 22)]
roll_nos = [stu[0] for stu in students]
names = [stu[1] for stu in students]
ages = [stu[2] for stu in students]
print(f"Roll Numbers: {roll_nos}")
print(f"Names: {names}")
print(f"Ages: {ages}")
print("-" * 50)

# Question 3: Calculate days between two date tuples
from datetime import date
print("3 Calculate Number of Days Between Two Dates:")
date1 = (2025, 4, 10)  # format: (year, month, day)
date2 = (2024, 4, 18)
d1 = date(*date1)
d2 = date(*date2)
diff = abs((d2 - d1).days)
print(f"Number of days between {date1} and {date2}: {diff}")
print("-" * 50)

# Question 4: Sort list of food tuples by price descending
print("4 Sort Food Items by Price (Descending):")
menu = [("Burger", 99), ("Pizza", 199), ("Sandwich", 79), ("Fries", 49)]
sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)
for item, price in sorted_menu:
    print(f"{item}: ₹{price}")
print("-" * 50)

# Question 5: Remove empty tuples from list
print("5 Remove Empty Tuples from List:")
items = [(), (1, 2), (), (3, 4, 5), (), ('A',)]
filtered_items = [i for i in items if i]
print(f"List after removing empty tuples: {filtered_items}")
print("-" * 50)

# Question 6: Modify an element of a tuple (via conversion)
print("6 Modify an Element of a Tuple:")
my_tuple = (10, 20, 30)
print(f"Original Tuple: {my_tuple}")
temp_list = list(my_tuple)
temp_list[1] = 99  # Changing second element
my_tuple = tuple(temp_list)
print(f"Modified Tuple: {my_tuple}")
print("-" * 50)

# Question 7: Delete an element from a tuple (via conversion)
print("7 Delete an Element from a Tuple:")
my_tuple = (10, 20, 30, 40)
print(f"Original Tuple: {my_tuple}")
temp_list = list(my_tuple)
del temp_list[2]  # Delete element at index 2 (30)
my_tuple = tuple(temp_list)
print(f"Tuple after deletion: {my_tuple}")
print("-" * 50)
