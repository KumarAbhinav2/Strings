"""
Given a string, find the first non-repeating character in it and return its index.
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
"""

class Solution:

    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        for i, v in enumerate(s):
            if counts[v] == 1:
                return i
        return -1

    ## Time Complexity: O(N)
    ## Space Complexity: O(1)