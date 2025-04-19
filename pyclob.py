# 1. Complex Number Class
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def show(self):
        print(f"{self.r} + {self.i}i")

c1 = Complex(2, 3)
c2 = Complex(1, 4)
result = c1.add(c2)
print("1 Complex Addition: ", end=""); result.show()


# 2. Matrix Class (3x3)
class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def add(self, other):
        return [[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)]

m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])
print("2 Matrix Addition:", m1.add(m2))


# 3. Solid (Surface Area & Volume)
class Solid:
    def __init__(self, radius, height):
        self.r = radius
        self.h = height

    def area(self):
        return 2 * 3.14 * self.r * (self.r + self.h)

    def volume(self):
        return 3.14 * self.r * self.r * self.h

s = Solid(3,5)
print("3 Surface Area:", s.area())
print("   Volume:", s.volume())


# 4. Shape (Circle) Area & Perimeter
class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return 3.14 * self.r * self.r

    def perimeter(self):
        return 2 * 3.14 * self.r

c = Circle(7)
print("4 Circle Area:", c.area())
print("   Circle Perimeter:", c.perimeter())


# 5. Time Class
class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def add(self, other):
        total_min = self.m + other.m
        h = self.h + other.h + (total_min // 60)
        m = total_min % 60
        return Time(h, m)

t1 = Time(2, 45)
t2 = Time(1, 30)
sum_time = t1.add(t2)
print(f"5 Total Time: {sum_time.h} hrs {sum_time.m} min")


# 6. Date Class (Comparison)
class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def __eq__(self, other):
        return self.d == other.d and self.m == other.m and self.y == other.y

date1 = Date(18,4,2025)
date2 = Date(18,4,2025)
print("6 Dates are same!" if date1 == date2 else "Dates are different.")


# 7. Weather Class (__contains__)
class Weather:
    def __init__(self):
        self.conditions = ["Rain", "Snow", "Wind", "Sunny"]

    def __contains__(self, item):
        return item in self.conditions

w = Weather()
print("7 Is 'Snow' in weather list?", "Snow" in w)


# 8. String Class (Methods & Operator Overload)
class MyString:
    def __init__(self, text):
        self.text = text

    def __iadd__(self, other):
        self.text += other.text
        return self

    def toLower(self):
        return self.text.lower()

    def toUpper(self):
        return self.text.upper()

s1 = MyString("Hello")
s2 = MyString("World")
s1 += s2
print("8 String Concatenation:", s1.text)
print("   Lowercase:", s1.toLower())
print("   Uppercase:", s1.toUpper())






