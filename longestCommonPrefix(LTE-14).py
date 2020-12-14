"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        # getting the smallest string based on length, lcp driven by smallest string
        shortest = min(strs, key = len)
        for i, val in enumerate(shortest):
            # checking prefix common in rest of the strings
            for other in strs:
                if other[i] != val:
                    return shortest[:i]
        return shortest

