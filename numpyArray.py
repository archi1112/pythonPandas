import numpy as np

if __name__ == "__main__":
   a=np.array([
      [[1,2,3],[1,2,4],[1,2,3]],
      [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
   ])
   print(a.shape)
   # print the dimension of numpy array
   print(a.ndim)
   # prints total number of elements
   print(a.size)

# array with different data types
   b=np.array([
      [["One",2,3],[1,"Two",4],[1,2,"Three"]],
      [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
   ])
   # prints <U11 this means that datatype pof array is string with string less than 11 characters
   print(b.dtype)

   c=np.array([
      [["1",2,3],[1,"2",4],[1,2,"3"]],
      [[1, 2, 3], [1, 2, 4], [1, 2, 3]]
   ] , dtype=np.float32)

   # if we give the dtype it converts the string and numbers to that partucular dtype
   print(c[0][0][0])
   print(type(c[0][0][0]))