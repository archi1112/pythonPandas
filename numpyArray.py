import numpy as np

"""
1.shape()
2.dtype()
3.ndim()
4.zeroes()- fill with zeroes
5.ones()-fill with ones
6.full()-fill with a particular value
7.empty()-creates empty array with random/garbage values
8.arange()-create array starting from a number to partcular value with a skip
9.Difference in list and numpy array 
    ->multiplication
    ->addition
"""
if __name__ == "__main__":
    a = np.array([
        [[1, 2, 3], [1, 2, 4], [1, 2, 3]],
        [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
    ])
    print(a.shape)
    # print the dimension of numpy array
    print(a.ndim)
    # prints total number of elements
    print(a.size)

    # array with different data types
    b = np.array([
        [["One", 2, 3], [1, "Two", 4], [1, 2, "Three"]],
        [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
    ])
    # prints <U11 this means that datatype pof array is string with string less than 11 characters
    print(b.dtype)

    c = np.array([
        [["1", 2, 3], [1, "2", 4], [1, 2, "3"]],
        [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
    ], dtype=np.float32)

    # if we give the dtype it converts the string and numbers to that partucular dtype
    print(c[0][0][0])
    print(type(c[0][0][0]))

    """
   numpy array filling
   """

    d = np.full((2, 3), 4)
    print(d)

    # creates a 0's
    zeroArray = np.zeros((2, 3), np.float32)
    print(zeroArray)

    # creates an array of one's
    print(np.ones((2, 3)))

    # creates an empty array of garbage
    emptyArray = np.empty((5, 5, 5))
    print(emptyArray)

    # prints number from 0 to 100 with a skip of two
    values = np.arange(0, 100, 2)

# ===============================================================
# Mathematical operations
"""
1.Difference in list and numpy array (on list only addition is possible it concatenates two lists , 
other operators are not valid on the lists)
"""

listExample = [1, 2, 3, 4, 5]
numpyExample = np.array([1, 2, 3, 4, 5])

print(listExample * 3)  #prints [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(numpyExample * 3)  #prints array multiplying each element by 3

# addition
print("addition")
print(listExample + listExample)  #concatenates two lists [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(numpyExample + numpyExample)  #add each element od two lists [ 2  4  6  8 10]

#subtraction
print("subtraction")
# print(listExample - listExample)  #subtraction operator is not valid for lists will give error
print(numpyExample - numpyExample)  #subtract each element of two lists

# multiplication
print("multiplication")
# print(listExample * listExample)  # can't multiply sequence by non-int of type 'list'
print(numpyExample * numpyExample)

# division
print("division")
# print(listExample / listExample)  #unsupported operand
print(numpyExample / numpyExample)

# sqrt
print(np.sqrt(numpyExample))

# log
print(np.log2(numpyExample))