"""
Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
Only compress the string if it saves space.
"""

class Solution:

    def compressString(self, s):
        if not s or s is None:
            return s
        prev = s[0]
        res = ''
        count=0
        for char in s:
            if char == prev:
                count+=1
            else:
                res+= prev+(str(count) if count > 1 else '')
                prev = char
                count=1
        res += prev + (str(count) if count > 1 else '')
        return res if len(res) < len(s) else s

obj = Solution()
print(obj.compressString('AAABCCDDDD'))