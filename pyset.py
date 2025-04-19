#question1
words = ['apple', 'banana', 'grape', 'orange']

# Convert to uppercase and store in set
upper_case_set = set(map(str.upper, words))

print("Words in uppercase set:", upper_case_set)


#question2
import random

# Create a set of 10 random numbers between 15 and 45
random_numbers = set(random.randint(15, 45) for _ in range(10))
print("Original set:", random_numbers)

# Count numbers less than 30
count_below_30 = len([num for num in random_numbers if num < 30])
print("Count of numbers less than 30:", count_below_30)

# Delete all numbers greater than 35
filtered_set = {num for num in random_numbers if num <= 35}
print("Set after deleting numbers > 35:", filtered_set)


#question3
# Create empty set
names = set()

# Add 5 new names
names.update(["Alka", "Shreya", "Kinara", "Dhaval", "Ketan","Krisha"])
print("After adding names:", names)

# Modify one name (remove old, add new)
names.discard("Dhaval")  # Remove "David"
names.add("Dakshvi")     # Add "Daniel"
print("After modifying name:", names)

# Delete two names
names.discard("Shreya")
names.discard("Krisha")
print("After deleting two names:", names)


#question4
name_set = {"Aparna", "Amira", "Bobby", "ChintanBhatt", "Alka"}

# Separate names into two sets
a_names = {name for name in name_set if name.startswith('A')}
b_names = {name for name in name_set if name.startswith('B')}

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)



