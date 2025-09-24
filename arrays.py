
# import array as arr 
# Numbers = arr.array('i',[1,2,3,4,5])
# print(type(Numbers))

#updating an element:
# numbers =[1,2,3,4,5]
# numbers[0]=10
# print(numbers)

# #append
# numbers =[1,2,3,4,5]
# numbers.append(7)
# print(numbers)

# #insert():
# numbers.insert(2,6)
# print(numbers)

# #extend():
# numbers.extend([8,9])
# print(numbers)


# import numpy as np

# import array as arr
import numpy as np
#1D array
A1D=np.array([1,2,3,4,5])
print(A1D)
A2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A2D)

A1D=np.array([1,2,3,4,5])
print(A1D.size)

A2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A2D.shape)

print(A2D.dtype)

# A= np.array([1,2,3,4,5])
# L=[1,2,3,4,5]
# print(A+6)
# print(A-1)
# print(A*2)
# print(A/2)
# print(A//2)
# print(A**6)

# mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
# mat2=np.array([[4,7,2],[8,4,1],[7,8,9]])
# print(mat1 + mat2)
# print(mat1 - mat2)
# print(mat1 * mat2)
# #dat():
# print(np.dot(mat1,mat2))
# #transpose
# print(np.transpose(mat1*mat2)