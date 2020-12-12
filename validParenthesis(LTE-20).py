"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

class Solution:

    def isValid(self, s: str) -> bool:
        mymap = {'}':'{', ')':'(', ']':'['}
        # Stack to hold the values
        _stack = []
        for i in s:
            # closing bracker check in mymap
            if i in mymap:
                # get the nearest bracket (top in stack)
                top = _stack.pop() if _stack else '#'
                # check if the nearest bracket is the opening one or not
                if top != mymap[i]:
                    return False
            else:
                _stack.append(i)
        # if stack is empty that means valid expression
        return not _stack

    # Time complexity: O(n) because we simply traverse the given string one character at a time and
    #                   push and pop operations on a stack take O(1)O(1) time.
    # Space complexity: O(n) having separate stack