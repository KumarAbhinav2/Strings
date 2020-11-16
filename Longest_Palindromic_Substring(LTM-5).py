"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
"""

class Solution:

    def longestPalindrome(self, s):
        res= ''
        for c in range(len(s)):
            temp_str = self.getPalindrome(s, c, c)
            if len(temp_str) > len(res):
                res = temp_str

            temp_str = self.getPalindrome(s, c, c+1)
            if len(temp_str) > len(res):
                res = temp_str
        return res

    def getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left+1:right]


