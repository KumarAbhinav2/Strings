"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.
Find how many minimum characters are needed to be inserted to make the string a palindrome string.\

For example:
Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".

Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".
"""

from __init__ import duration
import unittest

class Solution:
    # @param A : string
    # @return an integer

    def ispalindrome(self, A):
        start = 0
        n = len(A)
        end = n-1
        while start < end:
            if A[start].isalnum() and A[end].isalnum():
                start_string = A[start].lower()
                end_string = A[end].lower()
                if start_string != end_string:
                    return 0
                else:
                    start +=1
                    end -=1
            elif not A[start].isalnum():
                start +=1
            elif not A[end].isalnum():
                end -=1
        return 1

    @duration
    def intuitive(self, A):
        string_to_insert = ''
        n = len(A)
        if self.ispalindrome(A):
            return 0
        for i in range(n-1, -1, -1):
            string_to_insert += A[i]
            if self.ispalindrome(string_to_insert+A):
                return len(string_to_insert)

    @duration
    def better(self, A):
        n = len(A)
        if n <= 1:
            return 0
        i, j, j_start = 0, n-1, n-1
        while i < j:
            if A[i] == A[j]:
                i +=1
                j -=1
            else:
                j = j_start-1
                j_start = j
                i = 0
        return n -1 - j_start

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = "ABC"
        self.input2 = "AACECAAAA"
        self.input3 = "MAM"
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res, 2)
        res = self.obj.intuitive(self.input2)
        self.assertEqual(res, 2)
        res = self.obj.intuitive(self.input3)
        self.assertEqual(res, 0)

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res, 2)
        res = self.obj.better(self.input2)
        self.assertEqual(res, 2)
        res = self.obj.better(self.input3)
        self.assertEqual(res, 0)


if __name__ == '__main__':
        unittest.main()







