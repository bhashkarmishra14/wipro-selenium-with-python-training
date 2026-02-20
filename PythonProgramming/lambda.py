#lambda functions - anonymous(nameless) functions, one line only
#syntax lambda arguments: expression
#it can have any number of arguments
#must have only one expression
#the expression is automatically returned
#functions - function name, arguments, return type, code
#normal function for add 2 numbers
def add(a,b):
    return a+b
print(add(5,3))
#lambda function
add = lambda a,b: a+b
print(add(5,3))
#square of a number
square = lambda x : x*x
print(square(5))
#check even or odd
even = lambda x: x%2 ==0
print(even(10))
#find the max of 2 numbers
max = lambda a,b : a if a>b else b
print(max(10, 30))
#methods in lambda
#filter, map, and reduce in built functions in lambda
# filter - select data - filtering the data
#map- transform the data
#reduce - aggregate the data
#filter
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2 ==0 ,numbers))
print(evens)
#filter the failed test cases
status = ['Pass', 'Fail', 'Pass', 'Fail']
failed = list(filter(lambda s:s == 'Fail', status))
print(failed)
#filter positives numbers nums = [-5, 10, -3, 7, 0, 2]
nums = [-5, 10, -3, 7, 0, 2]
positive_nums = list(filter(lambda n: n>=0,nums))
print(positive_nums)
#Filter non-empty strings data = ["hello", "", "world", "", "python"]
data = ["hello", "", "world", "", "python"]
non_emptystring = list(filter(lambda s: s !="",data))
print(non_emptystring)
#reduce - aggregate - combining many values to one single result
from functools import reduce
nums=[10,20,30,40]
print(reduce(lambda x,y: x+y, nums))
#multiply , maximum value, minimum value
from functools import reduce

nums = [10, 20, 30, 40]
print(reduce(lambda x, y: x + y, nums))
print(reduce(lambda x, y: x * y, nums))
print(reduce(lambda x, y: x if x > y else y, nums))
print(reduce(lambda x, y: x if x < y else y, nums))

#map- transform the data
nums = [10, 20, 30, 40]
squares = list(map(lambda x : x*x , nums))
print(squares)
#sorting in lambda
data = [(1,3),(4,1),(2,2)]
sorteddata = sorted(data, key=lambda x : x[1])
print(sorteddata)

marks = {"A": 75, "B": 90, "C": 60}
sorted_marks = dict(sorted(marks.items(),key=lambda x: x[1]))
print(sorted_marks)

print(list(filter(None, [0, "", None, 5, "Hi"])))
nums = [1, 2, 3]
f = map(lambda x: x * 2, nums)
nums.append(4)
print(list(f))
print(list(map(lambda x: x[0], ["python", "java", "c++"])))
print(list(map(lambda x: x.upper(), filter(lambda x: x.islower(), "PyThOn"))))
print(list(filter(lambda x: x > 2, map(lambda x: x + 1, [1, 2, 3]))))





