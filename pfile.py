import csv
import os
import pickle

# 1 Create a CSV File
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["RollNo", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([1, "Alka", 85, 78, 92])
    writer.writerow([2, "Kinara", 88, 75, 80])
print("CSV file 'students.csv' created.")


# 2 Read CSV as Dictionary & Calculate Total
data = {}
with open('students.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        data[row['RollNo']] = {'Name': row['Name'], 'Total': total}
print("\nData with Total Marks:", data)


# 3 Create vCard for Contact
name = "John Doe"
phone = "+911234567890"
email = "john@example.com"
vcard = f"BEGIN:VCARD\nFN:{name}\nTEL:{phone}\nEMAIL:{email}\nEND:VCARD"
with open("contact.vcf", "w") as file:
    file.write(vcard)
print("\nvCard 'contact.vcf' created.")


# 4 Create Subdirectory and Copy File
os.makedirs('NewFolder', exist_ok=True)
with open('sample.txt', 'w') as f:  # source file
    f.write("This is a test file.")

import shutil
shutil.copy('sample.txt', 'NewFolder/copied_sample.txt')
print("\nFile copied to 'NewFolder'.")


# 5 Copy and Convert to Uppercase
with open('sample.txt', 'r') as src, open('upper_sample.txt', 'w') as dest:
    for line in src:
        dest.write(line.upper())
print("\nContents copied and converted to uppercase in 'upper_sample.txt'.")


# 6 Merge Two Files Alternately
with open('file1.txt', 'w') as f: f.write("Line1_File1\nLine2_File1\n")
with open('file2.txt', 'w') as f: f.write("Line1_File2\nLine2_File2\nLine3_File2\n")

with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as out:
    lines1, lines2 = f1.readlines(), f2.readlines()
    for pair in zip(lines1, lines2):
        out.writelines(pair)
    out.writelines(lines1[len(lines2):] + lines2[len(lines1):])
print("\nFiles merged into 'merged.txt'.")


# 7 Serialize & Deserialize Employee Object
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

emp = Employee(101, "Emma", "2022-01-10", 50000)
with open("employee.pkl", "wb") as f:
    pickle.dump(emp, f)

with open("employee.pkl", "rb") as f:
    loaded_emp = pickle.load(f)
print(f"\nDeserialized Employee: {loaded_emp.empname}, Salary: {loaded_emp.salary}")


# 8 Delete Specific Words from a File
with open('textfile.txt', 'w') as f:
    f.write("This is a text file with the words a, the, and an.")

with open('textfile.txt') as f:
    text = f.read()

for word in [' a ', ' the ', ' an ']:
    text = text.replace(word, ' ')

with open('cleaned_textfile.txt', 'w') as f:
    f.write(text)

print("\n'cleaned_textfile.txt' created after removing 'a', 'the', 'an'.")
