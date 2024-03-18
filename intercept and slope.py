# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:46:16 2024

@author: Tripti
"""
import math
X=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
Y=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
sum_of_squares=0
sum_of_x=0
d=0
sum_of_y=0
predicted_values=0
for i in X:
    sum_of_x=sum_of_x+i
for i in X:
    sum_of_squares=sum_of_squares+i**2
for i in Y:
    sum_of_y=sum_of_y+i
(sum_of_y)
for i in range(len(X)):
    d=d+(X[i]*Y[i])
print('sum_xy=',d)    
print('sum_of_squares)=',sum_of_squares)
Slope=(len(X)*d-sum_of_x*sum_of_y)/(len(X)*sum_of_squares-sum_of_x**2)
print('Slope=', Slope)
intercept=(sum_of_y-Slope*sum_of_x)/(len(X))
print("intercept=", intercept )      


    