import re

# Sample resumes
resumes = [
"""
Name: John Smith
Email: john.smith@gmail.com
Mobile: +91 9876543210
Skills: Python, SQL, Machine Learning, NLP
Experience: 3 years
""",

"""
Name: Priya Sharma
Email: priya123@yahoo.com
Phone: 9123456789
Skills: Java, SQL
Experience: 1 year
""",

"""
Name: David Wilson
Email: david.wilson@company.com
Contact: 9876501234
Skills: Python, Java, SQL
Experience: 5 years
"""
]

# Technical skills to search
technical_skills = ["Python", "Java", "SQL", "Machine Learning", "NLP"]

print("=" * 60)
print("RESUME INFORMATION EXTRACTION")
print("=" * 60)

eligible_candidates = []

for resume in resumes:

    # Extract Name
    name = re.search(r"Name\s*:\s*([A-Za-z ]+)", resume)
    name = name.group(1).strip() if name else "Not Found"

    # Extract Email
    email = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume)
    email = email.group() if email else "Not Found"

    # Extract Mobile Number
    mobile = re.search(r"(\+91\s?)?[6-9]\d{9}", resume)
    mobile = mobile.group() if mobile else "Not Found"

    # Extract Skills
    skills_found = []
    for skill in technical_skills:
        if re.search(skill, resume, re.IGNORECASE):
            skills_found.append(skill)

    # Extract Experience
    exp = re.search(r"(\d+)\s*year", resume, re.IGNORECASE)
    experience = int(exp.group(1)) if exp else 0

    # Display Summary
    print("\nCandidate Profile")
    print("-" * 30)
    print("Name       :", name)
    print("Email      :", email)
    print("Mobile     :", mobile)
    print("Skills     :", ", ".join(skills_found))
    print("Experience :", experience, "Years")

    # Eligibility Check
    if experience >= 2 and "Python" in skills_found:
        eligible_candidates.append(name)

print("\n" + "=" * 60)
print("ELIGIBLE CANDIDATES")
print("=" * 60)

if eligible_candidates:
    for candidate in eligible_candidates:
        print(candidate)
else:
    print("No eligible candidates found.")