# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a < 0 or b < 0 or c < 0:
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly GREATER than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == c and a == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'


## All Issues found in code
# Should move the checker for our values being integers above the checks of greater than 0 less
# than 200.

# line 34, the '=' symbols are unnecessary. 

# line 34, the if statement for 'b<=b' will always result in a return
# of 'InvalidInput'

# line 40, the semicolon after 'InvalidInput' is unnecessary

# line 46, the logic for deciding if the inputs are a triangle is wrong,
# change the '-' symbols to '+' symbols.

# line 50, the logic for equilateral triangles is wrong,
# its missing a check for the value of c

# line 52, the logic for right triangle is wrong, instead of multiplying
# our values by 2 with a single '*' we should write it as 'a ** 2)

# line 54, the logic for scalene triangles is wrong, last check should
# be 'a!=c'
    
# line 57, Isosceles is spelled incorrectly