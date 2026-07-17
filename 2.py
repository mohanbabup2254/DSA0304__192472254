import re

# Product List
products = [
    "Apple iPhone 15",
    "Apple MacBook Air",
    "Samsung Galaxy S24",
    "Samsung Smart TV",
    "Sony Headphones",
    "Dell Laptop",
    "HP Laptop",
    "Lenovo ThinkPad",
    "Wireless Mouse",
    "Bluetooth Speaker",
    "Python Programming Book",
    "Java Programming Book",
    "SQL Database Guide"
]

# Function to perform product search
def search_products(pattern, description, flags=0):
    print("\n" + "=" * 50)
    print(description)
    print("=" * 50)

    matches = []

    for product in products:
        if re.search(pattern, product, flags):
            matches.append(product)

    if matches:
        print("Matching Products:")
        for item in matches:
            print("-", item)
    else:
        print("No matching products found.")

    print("Total Matches:", len(matches))

# 1. Exact Keyword Search
keyword = input("Enter exact keyword: ")
pattern = r"\b" + re.escape(keyword) + r"\b"
search_products(pattern, "Exact Keyword Search")

# 2. Prefix Search
prefix = input("\nEnter prefix: ")
pattern = r"^" + re.escape(prefix)
search_products(pattern, "Prefix Search")

# 3. Suffix Search
suffix = input("\nEnter suffix: ")
pattern = re.escape(suffix) + r"$"
search_products(pattern, "Suffix Search")

# 4. Partial Keyword Search
partial = input("\nEnter partial keyword: ")
pattern = re.escape(partial)
search_products(pattern, "Partial Keyword Search")

# 5. Case-Insensitive Search
case_word = input("\nEnter keyword for case-insensitive search: ")
pattern = re.escape(case_word)
search_products(pattern, "Case-Insensitive Search", re.IGNORECASE)