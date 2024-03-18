# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 09:30:59 2024

@author: Tripti
"""
A=[8,15,24,3]
P=[10,12,26,0]
B =0
for i in range(len(A)):
    B=B+abs(A[i]-P[i])
print(B/len(A))   
     