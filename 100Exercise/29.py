'''
Exercise 29 - Liquid Volume Calculator
Section 2, Lecture 62

Question:  Please write a function that calculates liquid volume in a sphere using the following formula. The radius r  is always 10, so consider making it a default parameter.


You can then test your solution by passing 2 for h and you should get the expected output.

Expected output:

4071.5040790523717
'''

from math import pi

def acc (r,h,p=pi):
   # r = float(r)
   # h = float(h)
    return ((4*p*(r**3))/3) - ((p*(h**2)*(3*r - h))/3)

print("Result: ",acc(10,2))
