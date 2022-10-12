from math import sqrt as sq
from tkinter import N, Y
a = int(input("enter the coefficient of x^2 in the equation: "))
b = int(input("Enter the coefficient of x in the equation: "))
c = int(input('Enter the value of C: '))
D = (b**2 - (4*a*c))
if D < 0:
    print("The equation has no real roots, would you like to view the complex roots")
else:
    y = sq((b**2 - (4*a*c)))   
    x1 = (-b + y)/(2*a)
    x2 = (-b - y)/(2*a)
    print (f'The roots of {a}x^2 +{+b}x +{+c} are x1 = {x1} and x2 =1 {x2}') 

# I was not able to provide a solution to c.
