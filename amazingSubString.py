"""
You are given a string S, and you have to find all the amazing substrings of S.
Amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).

Input
    ABEC

Output
    6
Explanation
Amazing substrings of given string are :
1. A
2. AB
3. ABE
4. ABEC
5. E
6. EC
here number of substrings are 6 and 6 % 10003 = 6.
"""
from __init__ import duration
import unittest


class Solution:

    @duration
    def intuitive(self, A):
        vowels = 'aeiouAEIOU'
        result = []
        n = len(A)
        for i in range(n):
            if A[i] in vowels:
                substring = ''
                while i <= n-1:
                    substring += A[i]
                    result.append(substring)
                    i += 1
        return len(result) % 10003

    @duration
    def better(self, A):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ans = 0
        for i in range(len(A)):
            if A[i] in vowels:
                ans = ans + (len(A)-i) % 10003
        return ans


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = "kFbwEBGMTPcOVqenWEempRwOsjuxgMEhohXKqSxZWcqUuDHsRAGNTzwBYvVmTfPCwzFomjtTKLKjUCzHuNaAVoYoDysQWphGyexu"
        self.input2 = "ABEC"
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res, 1033)
        res = self.obj.intuitive(self.input2)
        self.assertEqual(res, 6)

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res, 1033)
        res = self.obj.better(self.input2)
        self.assertEqual(res, 6)


if __name__ == '__main__':
        unittest.main()

