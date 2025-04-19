# 1 Concatenate Three Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
final_dict = {**dict1, **dict2, **dict3}
print("Combined Dictionary:", final_dict)


# 2 Check if a Dictionary is Empty
my_dict = {}
if not my_dict:
    print("\nDictionary is empty.")
else:
    print("\nDictionary is not empty.")


# 3 Department-wise Min & Max Salary
employees = [
    {'dept': 'HR', 'roll': 101, 'salary': 25000},
    {'dept': 'HR', 'roll': 102, 'salary': 30000},
    {'dept': 'IT', 'roll': 103, 'salary': 45000},
    {'dept': 'IT', 'roll': 104, 'salary': 40000}
]

dept_salaries = {}
for emp in employees:
    dept = emp['dept']
    salary = emp['salary']
    dept_salaries.setdefault(dept, []).append(salary)

print("\nDepartment-wise Min and Max Salary:")
for dept, salaries in dept_salaries.items():
    print(f"{dept} - Min: {min(salaries)}, Max: {max(salaries)}")


# 4 Frequency of Characters in a String
input_str = input("\nEnter a string: ")
frequency = {}
for char in input_str:
    frequency[char] = frequency.get(char, 0) + 1
print("Character Frequencies:", frequency)


# 5 Grocery Bill Calculation
prices = {'apple': 60, 'banana': 20, 'milk': 45, 'bread': 30}
quantities = {'apple': 2, 'banana': 5, 'milk': 1, 'bread': 3}

total_bill = sum(prices[item] * quantities.get(item, 0) for item in prices)
print("\nTotal Grocery Bill: ₹", total_bill)
