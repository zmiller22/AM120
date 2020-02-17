#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 16:49:52 2020

@author: zack
"""
import numpy as np

A = np.matrix([[-8,-2,-7],[-4,-2,-2],[-6,-7,-0]]);
B = np.matrix([[-1-3j,-8-10j,0-3j],[-7-3j,-4-9j,-3-2j],[11-3j,-16-12j,6-5j]])
P = np.matrix([[2,-3],[2,-4]])

# )3ii 
print(np.linalg.det(B))
print()

# )7ii
[D,V] = np.linalg.eig(B)
print(D)
print(V)
print()

# )7iii 
D = np.linalg.eig(A)[0]
print(D)
print()
