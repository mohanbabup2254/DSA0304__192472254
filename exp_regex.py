import re

# Sample text
text = "Contact me at student123@gmail.com or call 9876543210."

print("Original Text:", text)

# 1. Match at beginning
match = re.match(r"Contact", text)
if match:
    print("Match at beginning:", match.group())

# 2. Search for phone number
search = re.search(r"\d{10}", text)
if search:
    print("Phone Number Found:", search.group())

# 3. Find all emails
emails = re.findall(r"\S+@\S+", text)
print("Emails Found:", emails)

# 4. Replace phone number
new_text = re.sub(r"\d{10}", "XXXXXXXXXX", text)
print("Updated Text:", new_text)