#dictionary items-key values
#similar to list and tuples
#for integers , tuples and strings - keys must be immutable
#list cannot be used in the key for the dict as it is mutable in nature
country = {
    "India": "Delhi",
    "Canada": "Ottawa",
    "England": "London"
}
print(country)
#access the values of the dictionary
print(country["Canada"])
# add elements
country["Italy"]= "Rome"
print(country)
#remove elements
del country["India"]
print(country)
#clear
# country.clear()
# print(country)
#iterate among country
for coun in country:
    print(coun)
#length of the dict
print(len(country))
#for integers , tuples and strings - keys must be immutable
#integer as a key
my_dict = {1:"one", 2:"two", 3:"three"}
print(my_dict)
my_dict = {1:"four", 2:"two", 3:"three", 1:"one"}
print(my_dict)
#for integer keys must be immutable
#for tuples as a key
my_dict = {(1,2): "one two", 3: "three"}
print(my_dict)
my_dict = {(1,2): "one two" , 3:"three", 3:"four"}
print(my_dict)
#list as key
# my_dict = {1: "Hello", [1 , 2]: "There you"}
# print(my_dict)
d = {"a": 1, "b": 2, "c": 3}

# pop()  removes key and returns value
print(d.pop("b"))
print(d)

# update()  adds / updates key-value pairs
d.update({"d": 4})
print(d)

# keys()  returns all keys
print(d.keys())

# values()  returns all values
print(d.values())

# popitem()  removes last inserted item
print(d.popitem())
print(d)

# copy()  creates a copy
d2 = d.copy()
d2["a"] = 100
print(d)
print(d2)
#dict inside the list
employees = [
    {"id": 1 , "name": "Bhashkar", "role": "SE"},
    {"id": 2 , "name": "Harsha", "role": "QA"},
    {"id": 3 , "name": "Ravi", "role": "Dev"}
]
print(employees[0])
print(employees[0]["name"])
for emp in employees:
    print(emp["name"], emp["role"])
employees.append({"id": 4, "name": "Sita", "role": "Tester"})
print(employees)
employees.pop(0)
print(employees)
#search a item in the list
for emp in employees:
    if emp["name"] == "Harsha":
        print(emp)


