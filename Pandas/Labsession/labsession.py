import pandas as pd
import numpy as np

# 1. Create a DataFrame containing missing (None/NaN) values
data = {
    "Name": ["Ram", "Sam", "John", "Priya", "Amit"],
    "Age": [25, None, 28, 22, 30],
    "Salary": [40000, 50000, None, 38000, 60000],
    "Department": ["HR", "IT", "IT", "Finance", "HR"],
    "City": ["Delhi", "Bangalore", "Mumbai", "Bangalore", "Bangalore"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Detect missing values
print("\nMissing Values:")
print(df.isnull())

# 3. Replace missing values with 0
df_filled = df.fillna(0)
print("\nAfter replacing missing values with 0:")
print(df_filled)

# 4. Drop rows containing missing values
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:")
print(df_dropped)

# 5. Sort the DataFrame by Age in ascending order
sorted_age = df_filled.sort_values(by="Age", ascending=True)
print("\nSorted by Age (ascending):")
print(sorted_age)

# 6. Sort the DataFrame by Salary in descending order
sorted_salary = df_filled.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (descending):")
print(sorted_salary)

# 7. Groupby Department and find average Salary per department
avg_salary = df_filled.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:")
print(avg_salary)

# 8. Total Salary per department
total_salary = df_filled.groupby("Department")["Salary"].sum()
print("\nTotal Salary per Department:")
print(total_salary)

# 9. Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df_filled[(df_filled["Age"] > 25) & (df_filled["City"] == "Bangalore")]
print("\nEmployees Age > 25 and City = Bangalore:")
print(filtered)

# 10. Create new column Tax (10% of Salary) using apply()
df_filled["Tax"] = df_filled["Salary"].apply(lambda x: x * 0.10)
print("\nDataFrame with Tax column:")
print(df_filled)