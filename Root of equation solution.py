from math import sqrt as sq
from tkinter import N, Y
import numpy as np
import cmath

a = int(input("enter the coefficient of x^2 in the equation: "))
b = int(input("Enter the coefficient of x in the equation: "))
c = int(input('Enter the value of C: '))
D = (b**2 - (4*a*c))
op = np.array([1, -1])
x1,x2 = (-1*b + op*(D ** 0.5 ))/2*a
w = u'\ax\u2703'
if D < 0:
    ans = input("The equation has no real roots, would you like to view the complex roots? would you like to view the roots, enter yes to view them, press any other key to exit ")
    if ans.lower == 'yes':
        print (f'The roots of {w} +{+b}x +{+c} are x1 = {x1} and x2 = {x2}')
    else:
        print ('you are welcome')    

else:
    print (f'The roots of {w} +{+b}x +{+c} are x1 = {x1} and x2 ={x2}')


