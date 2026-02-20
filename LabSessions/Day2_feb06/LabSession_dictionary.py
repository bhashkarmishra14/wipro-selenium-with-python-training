# Create a dictionary (roll number → student name)
students = {
    101: "Amit",
    102: "Riya",
    103: "Rahul"
}

# Print the dictionary
print("Dictionary:", students)

# Access value of an existing key
print("Value for key 102:", students[102])

# Access value of a key that does NOT exist (safe way)
print("Value for key 105:", students.get(105))   # returns None

# Update value of an existing key
students[103] = "Rohit"
print("After updating key 103:", students)

# Delete a key using del
del students[101]
print("After deleting key 101 using del:", students)

# Delete a key using pop()
students.pop(102)
print("After deleting key 102 using pop():", students)

# Find number of key–value pairs
print("Number of key-value pairs:", len(students))

# Print only keys
print("Keys:", students.keys())

# Print only values
print("Values:", students.values())

# Print key–value pairs
print("Key-Value pairs:", students.items())
