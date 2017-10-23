import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array

a[0] = 5                  # Change an element of the array

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]


a1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a1)
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b1 = a1[:4, 0:1]
print(b1)
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.

print(a1[0,1])   # Prints "2"
b1[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_height = np.array(height)
np_weight = np.array(weight)
print(np_weight)