"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above
(there may be multiple ways). For example, "111" can have each of its "1"s be mapped into 'A's to make "AAA",
or it could be mapped to "11" and "1" ('K' and 'A' respectively) to make "KA". Note that "06" cannot be mapped into
'F' since "6" is different from "06".

Given a non-empty string num containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

class Solution1:

    def numDecodings(self, s):
        self.cache = {}
        if not s:
            return 0
        return self.rec(0, s)

    def rec(self, idx, s):
        # check if we have entry in cache, reduces complexity here
        if idx in self.cache:
            return self.cache[idx]
        if idx == len(s):
            return 1
        # In case we encounter zero, we return 0
        if s[idx] == "0":
            return 0
        if idx == len(s) - 1:
            return 1
        # recursion on 2 digit selection only if they are in valid char range
        ans = self.rec(idx + 1, s) + (self.rec(idx + 2, s) if (int(s[idx:idx + 2]) <= 26) else 0)
        self.cache[idx] = ans
        return ans

    # Time: O(N) seem more than O(N) because of recursion but we have this cache check which helps in recursion
    #        tree pruning, thereby decoding for index only once
    # Space: O(N), dictionary for cache (len == string) and recursion stack with length N


class Solution2:

    def numDecodings(self, s):
        # array for dp, it stores the ways to decode s, dp[i] = Number of ways od decoding substring s[i]
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        # if we have zero as first char in string then number of ways to decode is o
        dp[1] = 1 if s[0] != 0 else 0
        # iterating from 2 as first two already filled
        for i in range(2, len(dp)):
            # if we can decode single digit
            if s[i-1] != 0:
                dp[i] = dp[i-1]

            # if we can decode with two digits
            # 01-09 not in map
            if 10<=int(s[i-2:i]) <=26:
                dp[i]+=dp[i-2]

        return dp[-1]

    # Time: O(N) , N length string
    # Space: O(N), length of DP array





obj = Solution()
obj.numDecodings("2326")
