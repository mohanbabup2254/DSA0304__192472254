import re

# Input from user
register_no = input("Enter Register Number: ")
email = input("Enter Institutional Email: ")
course_code = input("Enter Course Code: ")
semester = input("Enter Semester (1-8): ")
mobile = input("Enter Mobile Number: ")

print("\n===== VALIDATION RESULTS =====")

# 1. Validate Register Number
# Format: 22CS1012 (2 digits + 2 uppercase letters + 4 digits)
if re.fullmatch(r"\d{2}[A-Z]{2}\d{4}", register_no):
    print("Register Number : Valid")
    reg_valid = True
else:
    print("Register Number : Invalid")
    reg_valid = False

# 2. Validate Institutional Email
# Example: student@university.edu
if re.fullmatch(r"[A-Za-z0-9._%+-]+@university\.edu", email):
    print("Institutional Email : Valid")
    email_valid = True
else:
    print("Institutional Email : Invalid")
    email_valid = False

# 3. Validate Course Code
# Format: CS301, IT205, AI401
if re.fullmatch(r"[A-Z]{2,3}\d{3}", course_code):
    print("Course Code : Valid")
    course_valid = True
else:
    print("Course Code : Invalid")
    course_valid = False

# 4. Validate Semester
# Values: 1 to 8
if re.fullmatch(r"[1-8]", semester):
    print("Semester : Valid")
    sem_valid = True
else:
    print("Semester : Invalid")
    sem_valid = False

# 5. Validate Mobile Number
# Indian Mobile Number
if re.fullmatch(r"(\+91[- ]?)?[6-9]\d{9}", mobile):
    print("Mobile Number : Valid")
    mobile_valid = True
else:
    print("Mobile Number : Invalid")
    mobile_valid = False

# Final Registration Status
print("\n===== REGISTRATION STATUS =====")

if reg_valid and email_valid and course_valid and sem_valid and mobile_valid:
    print("Registration Successful")
else:
    print("Registration Failed")