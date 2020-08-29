"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""

class Solution:
    def decodeString(self, s: str) -> str:
        _stack = []
        num = 0
        string = ''
        for c in s:
            if c in '0123456789':
                num = num*10+int(c)
            elif c == '[':
                _stack.append(string)
                _stack.append(num)
                num=0
                string=''
            elif c.isalpha():
                string+=c
            elif c == ']':
                n = _stack.pop()
                p_str = _stack.pop()
                string = p_str+ string*n
        return string

    def decodeString2(self, s):
        num = ''
        _stack = []
        _stack.append(['', 1])
        for c in s:
            if c in '0123456789':
                num += c
            elif c == '[':
                _stack.append(['', int(num)])
                num = ''
            elif c.isalpha():
                _stack[-1][0] += c
            else:
                st, n = _stack.pop()
                _stack[-1][0] += st*n
        return _stack[0][0]


obj = Solution()
obj.decodeString("3[a]2[bc]")