# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:56:29 2023

@author: Tripti
"""
name=input("Enter Name: ")
age=int(input("Enter Age: "))
gender=input("Enter Gender: ")
comp_age=15
if(age>comp_age):
    if (gender=='female'):
        print("Hi "+name+" your age is greater than me. Can I call you Didi?")
        res=input()
        if(res=='yes'):
            print("Okay. Thankyou.")
        else:
            print("Okay. Sorry.")
    else:
        print("Hi "+name+" your age is greater than me. Can I call you Bhaiya?")
        res=input()
        if(res=='Yes'):
            print("Okay. Thankyou.")
        else:
            print("Okay. Sorry")
elif(age<comp_age):
    if(gender=='Female'):
        res=input()
        print("Hi "+name+" you are younger to me. Can I call you choti?")
        if (res=='Yes'):
             print("Okay. Thankyou.")
        else:
            print("Okay. Sorry.")
else:
    print("Hi "+name+". WOW! Your age is same as mine. We can be friends. Right?")
    res=input()
    if(res=='Yes'):
            print("Okay. Thankyou My Friend.")
    else:
            print("Okay. Sorry.")            
        