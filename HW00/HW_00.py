## APM120 HW-00
import numpy as np
from numpy import linalg
import scipy as scipy
import matplotlib.pyplot as plt
from math import pi

## Plot $f(x)=\cos(3x)$ vs $x$ for $x=(-2\pi,\pi)$:
x=np.arange(-2*pi,pi,0.1);
f=np.cos(3*x);
plt.figure(1);plt.clf();
plt.plot(x,f)
# always label axes and provide titles:
plt.xlabel('x')
plt.ylabel('f')
plt.title('f(x)=cos(3x)')
plt.show();

## Solve a linear equations $Ax=b$:
A = np.matrix([[-8,-2,-7],[-4,-2,-2],[-6,-7,-0]]);
b=np.array([3, 4, 1]);
print('determinant of A:')
print(np.linalg.det(A))
print('solution using matrix inverse is:')
x2=np.matmul(np.linalg.inv(A),b); print("x2=np.linalg.inv(A)="); print(x2)
print('checking that x is a solution; A*x2:')
print(np.matmul(A,x2.T))
print('b:')
print(b)

## Calculate the eigenvalues and vectors of $A$:
print('eigenvectors/ values of A:\n')
D,V=np.linalg.eig(A); D=np.diag(D);
print("V="); print(V);print("D="); print(D);

# Reminder: MATLAB indexes from 1, Python from 0.
## verify that V_1 is an eigenvector of A
print('A*v1:\n')
print(np.matmul(A,V[:,0]))
print('lambda1*v1:\n')
print(D[0,0]*V[:,0])

## verify that V_2 is an eigenvector of A
print('A*v2:\n')
print(np.matmul(A,V[:,1]))
print('lambda2*v2:\n')
print(D[1,1]*V[:,1])

## Calculate the eigenvalues and vectors of $B$:
B = np.matrix([[-1-3j,-8-10j,0-3j],[-7-3j,-4-9j,-3-2j],[11-3j,-16-12j,6-5j]])
print('eigenvectors/ values of A:\n')
D,V=np.linalg.eig(B); D=np.diag(D);
print("V="); print(V);print("D="); print(D);

# Reminder: MATLAB indexes from 1, Python from 0.
## verify that V_1 is an eigenvector of A
print('A*v1:\n')
print(np.matmul(A,V[:,0]))
print('lambda1*v1:\n')
print(D[0,0]*V[:,0])

## verify that V_2 is an eigenvector of A
print('A*v2:\n')
print(np.matmul(A,V[:,1]))
print('lambda2*v2:\n')
print(D[1,1]*V[:,1])
