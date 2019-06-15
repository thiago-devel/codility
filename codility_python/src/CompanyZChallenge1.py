'''
Write a function solution that, given an integer N, returns the smallest number with the same
number of digits. You can assume N is between 1 and 10^9 (a billion).

For example, given N = 125, the function should return 100. Given N = 10, the function should return
 10. Given N = 1, the function should return 0.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
import unittest
import math

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def solution(self, N):
        precision = len(str(N)) - 1
        if (precision == 0):
            return 0
        
        return 10 ** precision 
    
    def testSolution(self):
        self.assertEqual(self.solution(125), 100)
        self.assertEqual(self.solution(10), 10)
        self.assertEqual(self.solution(1), 0)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()