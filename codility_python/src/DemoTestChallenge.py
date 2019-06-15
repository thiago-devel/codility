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
        result = 0
        
        array = list(range(minN, maxN))
        #print(array)
        cA = list(dict.fromkeys(A));
        cA.sort()
        #print(cA)

        for i in range(0, len(cA)):
            if (array[i] != cA[i]):
                #print('I found the  {0} !'.format(array[i]))
                result = array[i]
                break
        
        
        if (result == 0):
            result = cA[len(cA) - 1] + 1
            
        #if (len(cA) == 1):
        #    result = cA[0] + 1
             
        if (result <= 0):
            result = 1
        
        
        return result
    
    
    def testSolution(self):
        self.assertEqual(self.solution([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(self.solution([1, 2, 3]), 4)
        self.assertEqual(self.solution([-1, -3]), 1)
        #self.assertEqual(self.solution([2]), 3)
        #self.assertEqual(self.solution([-1, 2]), 3)
        #self.assertEqual(self.solution([-1, 1, 3, 100, 200]), 201)
        #self.assertEqual(self.solution([-1000000, 1, 3, 1000000]), 1000001)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()