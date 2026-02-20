#create a student_id set integer type
stu_id = {112,113,114,115,115}
print(stu_id)
#create string type set
letters = {'a','b','c','d','e'}
print(letters)
#create a mixed set
mixed_set = {"hello",1,-7,8,9}
print(mixed_set)
#create empty set
empty_set = set()
#add elements to sets
# Q1 add()
s = {1, 2, 3}
s.add(2)                 # duplicate element
print(s)

# Q2 pop()
s = {10, 20, 30}
print(s.pop())           # removes random element
print(s)

# Q3 remove()
s = {1, 2, 3}
# s.remove(4)            # uncomment to see KeyError

# Q4 discard()
s = {1, 2, 3}
s.discard(4)             # no error
print(s)

# Q5 union()
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)

# Q6 intersection()
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)

# Q7 difference()
A = {1, 2, 3, 4}
B = {3, 4}
print(A - B)

# Q8 difference_update()
A = {1, 2, 3, 4}
B = {3, 4}
A -= B
print(A)

# Q9 symmetric_difference()
A = {1, 2, 3}
B = {3, 4}
print(A ^ B)

# Q10 issubset()
A = {1, 2}
B = {1, 2, 3}
print(A <= B)
print(A < B)

# Q11 issuperset()
A = {1, 2, 3}
B = {1, 2}
print(A >= B)
print(A > B)

# Q12 isdisjoint()
A = {1, 2}
B = {3, 4}
print(A.isdisjoint(B))

# Q13 update()
A = {1, 2}
B = {2, 3}
A.update(B)
print(A)

# Q14 clear()
s = {1, 2, 3}
s.clear()
print(s)

# Q15 copy()
A = {1, 2, 3}
B = A.copy()
B.add(4)
print(A)
print(B)
