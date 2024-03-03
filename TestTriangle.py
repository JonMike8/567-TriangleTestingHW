
import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # These tests check for invalid inputs
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(100,150,201),'InvalidInput','Not all values are less than 200')

    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(-2,-1,-5),'InvalidInput','All values are lower than 0')
    
    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle('2',10,12),'InvalidInput','Not all values are type int')

    # These tests check for valid triangles
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1 + 2 is not greater than 3')

    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(3,4,8),'NotATriangle','3 + 4 is not greater than 8')

    # These tests check for right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    
    # These tests check for scalene triangles
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(3,5,7),'Scalene','3,5,7 is a Scalene triangle')
    
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(4,11,8),'Scalene','4,11,8 is a Scalene triangle')
    
    # These tests check for equilateral triangles
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
    
    # These tests check for isosceles triangles
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,3),'Isosceles','2,2,3 should be isosceles')
    
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(5,5,7),'Isosceles','5,5,7 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

