import re

# Take input from user
text = input("Enter a sentence: ")

# Search for numbers in the input
result = re.search(r"\d+", text)

if result:
    print("Number found:", result.group())
else:
    print("No number found")