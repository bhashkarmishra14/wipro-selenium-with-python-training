# printing numbers from 1 to 5 using iter()
nums = [1, 2, 3, 4, 5]
iterator = iter(nums)

for i in iterator:
    print(i)


# returning even numbers using iter()
evens = [2, 4, 6, 8, 10]
iterator = iter(evens)

for i in iterator:
    print(i)


# explanation:
# iter() converts list into iterator
# for loop automatically fetches values using next()
# no need to define __iter__() and __next__()
