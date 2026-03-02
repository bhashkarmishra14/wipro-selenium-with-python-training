import numpy as np
#Changing the shapes


#reshape

a = np.arange(1,7)
print("Original array", a)

#reshape the array
reshaped = a.reshape(2, 3)
print("reshaped")

#flat =  return s ID iterator over the array
arr = np.array([[1,2], [3,4]])
for x in arr.flat:
    print(x)

#flatten - return the copy fo the array collapsed into one dimension
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel() - return a flattened array
arr = np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad() - returns a padded arrays with shape increased to pad_width
arr = np.array([1,2,3])
padded = np.pad(arr, 3, mode = 'constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)
#Transpose operations
#reorder the dimension of an array
#rows wil become the columns
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
#3 - rows - axis 1
#4 columns - axis 2



#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanging two axes of the array
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.swapaxes(arr, 0, 2)
print(new_arr)

#moveaxis() - Move specified axes to new positions
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

#joining Arrays
#concatenate()  - joining 2 arrays
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(np.concatenate((a,b), axis = 0))
print(np.concatenate((a,b), axis = 1))

#stack - Join the array along the new axis
#Adda a new dimensions
#all array must have the same shapes
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.stack((a,b), axis = 0))
print(np.stack((a,b), axis = 1))

#hstack - stack arrays horizontally (column-wise)
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.hstack((a,b)))
print(np.concatenate((a,b), axis = 1))

#vstack - stack arrays vertically (row-wise)
print(np.vstack((a,b)))
print(np.concatenate((a,b), axis = 0))
#column stack() - Stack 1D arrays as columns into a 2D arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.column_stack((a,b)))

#row_stack() - stack array row-wise
print(np.vstack((a,b)))

#Splittng Arrays
# split arrays into multiple sub arrays based on axis

arr = np.array([1,2,3,4,5,6])
result = np.split(arr, 3)
print(result)
#hsplit() - Split array horizontally (column - wise)
#works on 2D arrays

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(np.hsplit(arr2, 2))

#vsplit() - split array vertically (row -  wise)
arr2 = np.array([[1,2],
                 [3,4],
                 [5,6],
                [7,8]])
print(np.vsplit(arr2, 2))

#array_split() - similar to split(), but does not require equal division
arr = np.array([1,2,3,4,5])
print(np.array_split(arr, 3))
#Adding / Removing elements

#resize()- returns a new array with a specified shape

arr = np.array([1,2,3,4,5])
new_arr = np.resize(arr, (2,3))
print(new_arr)

# the elements will repeat in the new array
#returns a nnew array
#append()- appends values at the end of the array
arr = np.array([1,2,3])
new_arr = np.append(arr, [4,5])
print(new_arr)
#2D arrays

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

np.append(a, b, axis = 0)

#Inserting values before given index
arr = np.array([10,20,30])
new_arr = np.insert(arr, 1,15)
print(new_arr)

#Deletes elements along a specific axis
arr = np.array([10,20,30])
new_arr = np.delete(arr, 2)
print(new_arr)

#unique()
arr = np.array([1,2,3,4,5])
print(np.unique(arr))
#repeating
#repeat() - it is used to repeat  each element of an array a specified number of items
#each element is repeated twice
arr = np.array([1,2,3])
print(np.repeat(arr, 3))

#repeat in 2D array
arr2 = np.array([[1,2],
                [3,4]])
print(np.repeat(arr2, 2, axis = 0))

#tile()- the input array that will be repeated
my_array = np.array([1,2,3])
tiled_array = np.tile(my_array, 2)
print("Original array:", my_array)
print("Tiled array:", tiled_array)
#rearranging Elements
#flip() - reversing the order of elements along a given axis
#if axis= none --> reverse entire flattened array
#if axis = 0 --> reverse rows
# if axis = 1 --> reverse column
arr = np.array([1,2,3,4])
print(np.flip(arr))

#2D
arr2 = np.array([[1,2],
                 [3,4]])
print(np.flip(arr2, axis = 0)) #flip row
print(np.flip(arr2, axis = 1)) # flip column

#flipelr() - flip left - right (axis=1) - works only on 2D+ array
arr2 = np.array([[1,2,3],
                 [4,5,6]])
print(np.fliplr(arr2))
#flipud() - flip up-down (axis=0)
print(np.flipud(arr2))
#rolls() - rolls (rotates) elements along a given axis
arr2 = np.array([[1,2,3],
                 [4,5,6]])
np.roll(arr2, 2, axis=None)

#Sorting and Searching
#sort() returns a sorted copy of an array ( or sorts in place if using ndarray method)
arr = np.array([5,2,9,1])
sorted_arr = np.sort(arr)
print(sorted_arr)
#argsort() - returns indices that would sort the array return the index positions
arr = np.array([5,2,9,1])
sorted_arr = np.sort(arr)
print(sorted_arr)
indices = np.argsort(arr)
print(indices)
#lexsort() - used for sorting with multiple columns ( like sorting by last name then first name
#sort by a first
#then by b (secondary key)
#sorting happens from right to left
a = np.array([1,2,0,0])
b = np.array([1,0,1,0])
result = np.lexsort((b,a))
print(result)

#Changing Dimensions