#coding=utf-8
import numpy as np
A = np.mat(np.eye(4,4),int)
B = np.mat(np.full((4,4),20),int)
print(A+B)
print("-----------------")
print(A-B)
print("-----------------")
a=0.1
print(a*B)
print("=================")
data = [[1,2,3],[4,5,6],[7,8,9]]
C = np.mat(data,int)
print(C)
print("-----------------")
print(C.T)
print(np.linalg.matrix_rank(C))