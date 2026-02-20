# GENERATORS IN PYTHON
# Generator uses yield to return values one by one
# It saves memory and stops automatically when done


# generator to generate numbers from 1 to N
def numbers_upto_n(n):
    for i in range(1, n + 1):
        yield i


# generator to generate even numbers only
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


# generator to read a file line by line
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()  # returns one line at a time


# generator for Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# generator to simulate retry attempts (max 3 tries)
def retry_attempts(max_tries=3):
    for attempt in range(1, max_tries + 1):
        yield f"Attempt {attempt}"


# using generators
for i in numbers_upto_n(5):
    print(i)

for i in even_numbers(10):
    print(i)

# example file usage
# for line in read_file("sample.txt"):
#     print(line)

for i in fibonacci(5):
    print(i)

for attempt in retry_attempts():
    print(attempt)
