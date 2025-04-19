import random

# 1 Odd & Even Lists + Replace, Flatten, Sort
odds = [random.randrange(1, 20, 2) for _ in range(5)]
evens = [random.randrange(2, 20, 2) for _ in range(4)]
print("Original Odd List:", odds)
print("Original Even List:", evens)
odds[2] = evens  # Replace 3rd element with even list
print("After Replacement:", odds)
flattened = []
for item in odds:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)
flattened.sort()
print("Flattened & Sorted List:", flattened)


# 2 Search Positions in Random List
lst = [random.randint(1, 50) for _ in range(20)]
print("\nGenerated List:", lst)
num = int(input("Enter a number to search: "))
positions = [i for i, x in enumerate(lst) if x == num]
print(f"Positions of {num}:", positions if positions else "Not Found")


#3 Unique Random Numbers
random_nums = [random.randint(1, 30) for _ in range(50)]
unique = list(set(random_nums))
print("\nOriginal 50 Random Numbers:", random_nums)
print("Without Duplicates:", unique)


# 4 Split Positive & Negative Numbers
nums = [random.randint(-50, 50) for _ in range(30)]
positives = [n for n in nums if n >= 0]
negatives = [n for n in nums if n < 0]
print("\nOriginal Numbers:", nums)
print("Positive Numbers:", positives)
print("Negative Numbers:", negatives)


# 5 Convert Strings to Uppercase
strings = ["apple", "banana", "cherry", "date", "fig"]
uppercase = [s.upper() for s in strings]
print("\nOriginal Strings:", strings)
print("Uppercase Strings:", uppercase)


#6 Fahrenheit to Celsius Conversion
fahrenheit = [32, 68, 77, 104]
celsius = [(f - 32) * 5 / 9 for f in fahrenheit]
print("\nFahrenheit List:", fahrenheit)
print("Converted to Celsius:", celsius)


# 7 Stack Implementation
stack = []
while True:
    print("\nStack Menu: 1.Push 2.Pop 3.Display 4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        ele = input("Enter element to push: ")
        stack.append(ele)
    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is Empty!")
    elif choice == '3':
        print("Current Stack:", stack)
    elif choice == '4':
        break
    else:
        print("Invalid choice!")


# 8 Queue Implementation
queue = []
while True:
    print("\nQueue Menu: 1.Enqueue 2.Dequeue 3.Display 4.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        ele = input("Enter element to enqueue: ")
        queue.append(ele)
    elif choice == '2':
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is Empty!")
    elif choice == '3':
        print("Current Queue:", queue)
    elif choice == '4':
        break
    else:
        print("Invalid choice!")


#9 List Comprehension: Elements in List1 not in List2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8]
result = [n for n in list1 if n not in list2]
print("\nList1:", list1)
print("List2:", list2)
print("Numbers only in List1:", result)
