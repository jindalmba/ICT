# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:32:28 2024

@author:TRIPTI
"""
import math
X=[1.1,1.3,1.5,2,2.2,2.9,3,3.2,3.2,3.7,3.9,4,4,4.1,4.5,4.9,5.1,5.3,5.9,6,6.8,7.1,7.9,8.2,8.7,9,9.5,9.6,10.3,10.5]
Y=[39343,46205,37731,43525,39891,56642,60150,54445,64445,57189,63218,55794,56957,57081,61111,67938,66029,83088,81363,93940,91738,98273,101302,113812,109431,105582,116969,112635,122391,121872]
sum_of_squares=0
sum_of_x=0
d=0
sum_of_y=0
predicted=0
#intercept and slope
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
intercept= (sum_of_y-Slope*sum_of_x)/(len(X))
print("intercept=", intercept )
#predicted values 
predicted_salary=[]
for i in X:
    predicted=Slope*i+intercept
    predicted_salary=predicted_salary+[predicted]
print('predicted_salary=',predicted_salary)
#actual-predicted(MAE)
Actual_predicted=0
for i in range(len(Y)):
    Actual_predicted=Actual_predicted+abs((Y[i]-predicted_salary[i]))
print(Actual_predicted)
MAE=Actual_predicted/(len(X))
print('MAE=',MAE)
#MSE
Actual_predicted_square=0
for i in range(len(X)):
    Actual_predicted_square=Actual_predicted_square+abs((Y[i]-predicted_salary[i])**2)
#(Actual_predicted_square)
MSE=Actual_predicted_square/(len(X))
print('MSE=',MSE)
#MAPE
Actual_predicted_actual=0
for i in range(len(X)):
    Actual_predicted_actual=Actual_predicted_actual+abs(((Y[i]-predicted_salary[i])/(Y[i]))*100)
print('MAPE=',Actual_predicted_actual/len(X))
#predicted value using MSE(mean)
avg_actual_value=(sum_of_y)/(len(X))
print('Y predition=',avg_actual_value)
#MSE(mean)
actual_prediction_square=0
for i in range(len(Y)):
    actual_prediction_square=actual_prediction_square+((Y[i]-avg_actual_value)**2)
print('MSE(mean)=',actual_prediction_square/len(Y))
#R^2
R_square=((actual_prediction_square/len(Y))-MSE)/(actual_prediction_square/len(Y))
print('R_square=',R_square)                                                       








    