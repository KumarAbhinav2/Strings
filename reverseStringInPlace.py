"""
Implement a method to reverse a string in place

Input: Abhinav
Output: vanihbA
"""

## We cannot reverse a string in place because string are immutable, so we have to use another mutable
# data structure like list
import unittest

class Solution:

    def reverseString(self, chars):
        i = 0
        j = len(chars)-1
        while i < j:
            chars[i], chars[j] = chars[j], chars[i]
            i+=1
            j-=1
        return chars

class TestCase(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_success(self):
        input1 = list("Abhinav")
        expected = list("vanihbA")
        res = self.obj.reverseString(input1)
        self.assertEqual(res, expected)

if __name__ == '__main__':
    unittest.main()


