# all numbers should be integers
#step size should not be zero
# fetch values at the index
a= range(5)
print(a[1])
print(a[3])


a1 = range(2,5)
print(a1[1])

# for loop for range
a= range(2,5)
for i in a:
    print(i)

# for loop for range of 3 arguments
a= range(2,5,3)
for i in a:
    print(i)

# for loop for range of negative 3 arguments
a= range(2,15,-3)
for i in a:
    print(i)
# for loop for range of arguments with step size 0
#a= range(2,15,0)
#for i in a:
#    print(i)
#reverse printing
a= range(15,2,-1)
for i in a:
    print(i)
#senario : Allow 3 login attempts
for attempt in range(3):
    pin = input("Enter the pin:")
    if pin== "1234":
        print("Access granted")
        break
    else:
        print("Account locked")
#senario : Apply discount based on positions(index) of the item
prices = [100, 200, 300, 400]
for i in range(len(prices)):
    if i%2 == 0:
        print("Discount applied on item{1}")
#senario : simulate polling every second for 10 seconds
import time
for second in range(10):
    print("checking the status at {second} sec")
    time.sleep(1)