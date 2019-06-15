'''
Created on Jun 15, 2019

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def solution(self, A):
        minLEN = -1000000
        maxLEN = abs(minLEN)
        minN = 1
        maxN = 100000
        result = -1
        
        array = range(minN, maxN)
        cA = list(A);
        cA.sort()
        cB = list(dict.fromkeys(cA))
            
        for i in range(0, len(A)):
            if (array[i] != cB[i]):
                #print('I found the  {0} !'.format(array[i]))
                result = array[i]
                break
        
        if (result == -1):
            result = cB[len(cB) - 1] + 1
             
        if (result < 1):
            result = 1
        
        
        return result
    
    def testSolution(self):
        self.assertEqual(self.solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(self.solution([1, 2, 3]), 4)
        self.assertEqual(self.solution([-1, -3]), 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()