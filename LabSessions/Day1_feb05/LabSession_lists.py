#Write a Python program to get the largest number from a list.
numbers = [10, 45, 3, 99, 23]

largest = max(numbers)
print("Largest number:", largest)
#remove the even numbers from the lost
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [num for num in numbers if num % 2 != 0]

print(result)
#multiply the items in the list
numbers = [1, 2, 3, 4, 5]

result = 1

for num in numbers:
    result *= num

print("Product:", result)
