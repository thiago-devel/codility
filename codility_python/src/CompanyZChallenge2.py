'''
Write a function solution that, given two integers A and B, returns the maximum number of
repeated square root operations that can be performed using the numbers from the interval [A..B]
(both ends included) as starting points. Square root operations can be performed as long
as the result is still an integer.
For example, given A = 10, B = 20, the function should return 2. Starting with the integer 16, two 
square root operations can be performed: sqrt(16) = 4 and then sqrt(4) = 2.
Given A = 6000 and B = 7000, the function should return 3. Starting with integer 6561, three square 
root operations can be performed: sqrt(6561) = 81, sqrt(81) = 9 and sqrt(9) = 3.

Write an efficient algorithm for the following assumptions:
    * A and B are integers within the range [2..1,000,000,000];
    * A ≤ B.
@author: thiago-devel

'''
import unittest
import math

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def solution(self, A, B):
        if (A > B):
            return 0;
        
        sqrtA = math.ceil(math.sqrt(A));
        sqrtB = math.floor(math.sqrt(B));
        if (sqrtA > sqrtB):
            return 0;
        result = 1 + self.solution(sqrtA, sqrtB);
        
        return result        
    
    def testSolution(self):
        self.assertEqual(self.solution(10, 20), 2)
        self.assertEqual(self.solution(6000, 7000), 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()