
# nums = [1, 2, 3, 4, 5, 6]
# From a list of numbers:
# Filter even numbers
# Square them
# Find their sum
#2.salaries = [25000, 40000, 32000, 18000]
nums = [1, 2, 3, 4, 5, 6]

sum_nums = sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(sum_nums)
#2
salaries = [25000, 40000, 32000, 18000]

total_payout = sum(map(lambda x: x * 1.10, filter(lambda x: x > 30000, salaries)))

print(total_payout)

# =========================================================
# 1. Write a Python program to sort a list of tuples using Lambda
# =========================================================

data = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted list of tuples:", sorted_data)


# =========================================================
# 2. Write a Python program to extract year, month, date and time using Lambda
# =========================================================

from datetime import datetime

now = datetime.now()

year  = lambda d: d.year
month = lambda d: d.month
date  = lambda d: d.day
time  = lambda d: d.time()

print("Year:", year(now))
print("Month:", month(now))
print("Date:", date(now))
print("Time:", time(now))


# =========================================================
# 3. Write a Python script to concatenate dictionaries to create a new one
# =========================================================

d1 = {1: "A", 2: "B"}
d2 = {3: "C", 4: "D"}
d3 = {5: "E"}

new_dict = {**d1, **d2, **d3}
print("Concatenated Dictionary:", new_dict)



