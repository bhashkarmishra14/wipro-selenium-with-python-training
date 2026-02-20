#python program to sort a list of tuples using lambda
data=[(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data=sorted(data,key = lambda x:x[0])
print("sort",sorted_data)

#pyton program to extract year month date n time using lambda
data2={ "Year": 2026,
    "Month": "February",
    "Date": 6,
    "Time": "02:20"}
extracted=list(map(lambda v:v[1], data2.items()))
print(extracted)

#write a python script to concenate the following distionaries to create a new one
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {4:40, 5:50}
newdict = {}
newdict.update(dict1)
newdict.update(dict2)
newdict.update(dict3)
print("concatinated dict: ", newdict)