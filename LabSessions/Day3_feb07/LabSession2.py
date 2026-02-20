#1.Handle FileNotFoundError Exception When Opening a File

# Program to handle FileNotFoundError while opening a JSON file

import json

try:
    # Trying to open a JSON file that may not exist
    with open("C://Users//bhash//PycharmProjects//PythonAdvanceProgramming//Dataformats//employee.json", 'r') as file:
        data = json.load(file)

        # Printing JSON data
        print("JSON Data:", data)

except FileNotFoundError:
    # Executes if the JSON file is not found
    print("Error: JSON file not found. Please check the file name or path.")

except json.JSONDecodeError:
    # Executes if the JSON file has invalid format
    print("Error: Invalid JSON format in the file.")

else:
    # Executes if no exception occurs
    print("JSON file read successfully.")

finally:
    # Always executes
    print("JSON file operation completed.")

#2
#write a program to handle invalid user input

try:
    # Taking input from user
    number = int(input("Enter a number: "))

    # Performing an operation
    print("You entered:", number)

except ValueError:
    # Executes when user enters non-integer input
    print("Invalid input! Please enter a valid integer.")

else:
    # Executes if input is valid
    print("Input accepted successfully.")

finally:
    # Always executes
    print("Program execution finished.")

#Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()
import random
import string

# Pick one random alphabet
print(random.choice(string.ascii_letters))

# Create a random word using alphabets (5 letters)
print("".join(random.choice(string.ascii_letters) for _ in range(5)))

# Create a fixed length random word (10 letters)
print("".join(random.choice(string.ascii_letters) for _ in range(10)))







