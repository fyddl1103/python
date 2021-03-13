Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> A = np.array([1,2], [3,4])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    A = np.array([1,2], [3,4])
TypeError: Field elements must be 2- or 3-tuples, got '3'
>>> A = np.array([[1,2], [3,4]])
>>> A
array([[1, 2],
       [3, 4]])
>>> type(A)
<class 'numpy.ndarray'>
>>> A.ndim # 배열의 차원
2
>>> A[0,0]
1
>>> A[0,1]
2
>>> A[1,0]
3
>>> A[1,1]
4
>>> A.shape # 배열의 크기
(2, 2)
>>> A.dtype # 원소 자료형
dtype('int32')
>>> B = np.array([['A','B'], ['C','
			  
SyntaxError: EOL while scanning string literal
>>> B = np.array([['A','B'], ['C','D']])
>>> B.dtype
dtype('<U1')
>>> print(A.max(), A.mean(), A.min(), A.sum())
4 2.5 1 10
>>> print(A.max(), ' ',  A.mean(), A.min(), A.sum())
4   2.5 1 10
>>> A[0][0]
1
>>> A[A>A.mean()]
array([3, 4])
>>> A[A>1]
array([2, 3, 4])
>>> A.T
array([[1, 3],
       [2, 4]])
>>> A.T # A.transpose()와 같음
array([[1, 3],
       [2, 4]])
>>> A.transpose()
array([[1, 3],
       [2, 4]])
>>> A.flatten() # 다차원배열을 1차원배열로 변경
array([1, 2, 3, 4])
>>> ## 연산
>>> np.add(A,A) # A + A
array([[2, 4],
       [6, 8]])
>>> np.subtract(A,A) # A - A
array([[0, 0],
       [0, 0]])
>>> np.multiply(A,A) # A * A
array([[ 1,  4],
       [ 9, 16]])
>>> np.divide(A,A) # A / A
array([[1., 1.],
       [1., 1.]])
>>> B = np.array([10, 100])
>>> A * B
array([[ 10, 200],
       [ 30, 400]])
>>> B.dot(B) # B * B (1,2) * (2,1) = 1*1
10100
>>> A.dot(B) # 2*1
array([210, 430])
>>> 