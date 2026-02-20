# Write a regex to check if a string contains only digits.
# Write a pattern to match a 10-digit mobile number.
# Find all lowercase letters in a string.
# Extract all uppercase letters from a sentence.
# Match a string that starts with "Hello".
# Match a string that ends with "world".
# Find all words separated by spaces.
# Match exactly 5 characters.
# Find all occurrences of the word "python" (case-sensitive).
# Replace all spaces in a string with underscores.

import re
#1
text = "123456"
print(bool(re.findall(r"^\d", text)))

# 2️
mobile = "9876543210"
print(bool(re.findall(r"^\d{10}", mobile)))

#3️
text = "Hello World ABC xyz"
print(re.findall(r"[a-z]", text))

#4️
print(re.findall(r"[A-Z]", text))

#5
text = "Hello everyone"
print(re.findall(r"Hello", text))

#6️
text = "Hello world"
print(re.findall(r"world", text))

#7
text = "Python is very powerful"
print(re.findall(r"\w", text))

#8
text = "Hello"
print(re.findall(r".{5}", text))

#9
text = "python is good. Python is powerful. python!"
print(re.findall(r"python", text))

#10
text = "Python is very powerful"
print(re.sub(r"\s", "_", text))
