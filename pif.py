 #question 1
def largest_smallest_two():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if a > b:
        print(f"Largest: {a}, Smallest: {b}")
    elif b > a:
        print(f"Largest: {b}, Smallest: {a}")
    else:
        print("Both numbers are equal.")

if __name__ == "__main__":
    largest_smallest_two()


#question 2
def odd_or_even():
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")

if __name__ == "__main__":
    odd_or_even()


#question 3
def is_leap_year():
    year = int(input("Enter a year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

if __name__ == "__main__":
    is_leap_year()


#question 5    
def is_valid_triangle():
    a = int(input("Enter angle 1: "))
    b = int(input("Enter angle 2: "))
    c = int(input("Enter angle 3: "))
    if a + b + c == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

if __name__ == "__main__":
    is_valid_triangle()

#question 6
def check_divisible_by_10():
    num = int(input("Enter a number: "))
    if num % 10 == 0:
        print(f"{num} is divisible by 10.")
    else:
        print(f"{num} is NOT divisible by 10.")

if __name__ == "__main__":
    check_divisible_by_10()


#question7
def check_age():
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a Minor.")
    else:
        print("You are a Major.")

if __name__ == "__main__":
    check_age()


#question8
def count_number_of_digits():
    num = int(input("Enter a number: "))
    digit_count = len(str(abs(num)))   #Handles negative numbers too!
    print(f"The number {num} has {digit_count} digit(s).")

if __name__ == "__main__":
    count_number_of_digits()


#question9
def absolute_value():
    num = float(input("Enter a number: "))
    result = abs(num)  # abs() returns the non-negative value.
    print(f"The absolute value of {num} is {result}.")

if __name__ == "__main__":
    absolute_value()

#question10
def area_vs_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))

    area = length * breadth
    perimeter = 2 * (length + breadth)

    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

    if area > perimeter:
        print("Area is greater than Perimeter.")
    elif area < perimeter:
        print("Perimeter is greater than Area.")
    else:
        print("Area and Perimeter are equal.")

if __name__ == "__main__":
    area_vs_perimeter()


#question11
def check_colinear():
    print("Enter coordinates for 3 points:")

    x1, y1 = map(float, input("Point 1 (x,y): ").split())
    x2, y2 = map(float, input("Point 2 (x,y): ").split())
    x3, y3 = map(float, input("Point 3 (x,y): ").split())

    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        print("The points lie on the same straight line (Colinear).")
    else:
        print("The points do NOT lie on the same straight line.")

if __name__ == "__main__":
    check_colinear()


#question12
import math

def point_circle_relation():
    print("Enter coordinates of the point:")
    x, y = map(float, input("Point (x y): ").split())

    print("Enter center of the circle:")
    h, k = map(float, input("Center (h k): ").split())

    r = float(input("Enter the radius of the circle: "))

    distance = math.sqrt((x - h) ** 2 + (y - k) ** 2)

    if distance < r:
        print("The point lies inside the circle.")
    elif distance == r:
        print("The point lies on the circle.")
    else:
        print("The point lies outside the circle.")

if __name__ == "__main__":
    point_circle_relation()


#question13
def num_to_words():
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    num = int(input("Enter a number (0-19): "))

    if 0 <= num <= 19:
        print(f"The word for {num} is '{words[num]}'.")
    else:
        print("Number is out of range! Please enter a number between 0 and 19.")

if __name__ == "__main__":
    num_to_words()



#question14
def student_result():
    marks = []

    for i in range(1, 4):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 3
    status = "Pass"

    grades = []

    for mark in marks:
        if mark == -1:
            grades.append("NA")
            status = "Fail"
        elif mark <= 39:
            grades.append("F")
            status = "Fail"
        elif mark <= 44:
            grades.append("P")
        elif mark <= 49:
            grades.append("C")
        elif mark <= 54:
            grades.append("B")
        elif mark <= 59:
            grades.append("B+")
        elif mark <= 69:
            grades.append("A")
        elif mark <= 79:
            grades.append("A+")
        elif mark <= 100:
            grades.append("O")
        else:
            grades.append("Invalid")

    print(f"\nTotal Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Result: {status}")
    print(f"Grades for each subject: {grades}")

if __name__ == "__main__":
    student_result()

    
    
    
