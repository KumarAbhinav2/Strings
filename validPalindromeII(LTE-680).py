"""
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
"""

class Solution:

    def validPalindrome(self, s):
        i=0
        j=len(s)-1
        while i < j:
            if s[i]!=s[j]:
                # then either i -> j-1 will be palindromic or i+1 -> j will be palindromic
                first, sec = s[i:j], s[i+1:j+1]
                return first==first[::-1] or sec==sec[::-1]
            i+=1;j-=1
        return True

    # Time Complexity: O(N)
    # Space Complexity: O(N), s[i:j], s[i+1:j+1] story two additional strings and inplace reverse

    def validPalindrome2(self, s):

        i, j = 0, len(s)-1
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return self.validPalindromeTill(s, i+1, j) or self.validPalindromeTill(s, i, j-1)
        return True

    def validPalindromeTill(self, s, i,j):
        while i < j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

    # Time Complexity: O(n)
    # Space Complexitu: O(1)