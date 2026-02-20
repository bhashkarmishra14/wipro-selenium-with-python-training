#1.Write a Python function to check whether a number falls within a given range.
def in_range(n, start, end):
    return n in range(start, end + 1)

#2. Write a Python function to Print even numbers from 1 to 50
for i in range(2,51,2):
    print(i)
#3. Write a Python function to Sum of numbers from 1 to 100
def sum_1_to_100():
    return sum(range(1, 101))

print(sum_1_to_100())

#4. Print all numbers divisible by 5 between 1 and 100

for i in range(5, 101, 5):
    print(i)

#5.Create a list of numbers from 50 to 100 with a step of 5
for i in range(50,100,5):
    print(i)

#6. Print the square of each number from 1 to 10.
for i in range(1, 11):
    print(i ** 2)

#7. Print numbers between -10 and 10.
for i in range(-10, 11):
    print(i)

