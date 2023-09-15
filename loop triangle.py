# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:35:06 2023

@author: Tripti
"""
import turtle
t=turtle.Turtle()
a=200
b=120
for i in range(10):
    t.forward(a)
    t.left(b)
    t.forward(a)
    t.left(b)
    t.forward(a-10)
    t.left(b)
    t.forward(5)
    a=a-20


