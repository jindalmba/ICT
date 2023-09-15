# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:18:58 2023

@author: ASUS
"""
import turtle
t=turtle.Turtle()
a=100
b=90
for i in range(5):
    t.forward(a)
    t.left(b)
    t.forward(a)
    t.left(b)
    t.forward(a)
    t.left(b)
    t.forward(a-10)
    t.left(b)
    t.forward(10)
    a=a-20
    

