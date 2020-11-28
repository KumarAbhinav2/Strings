"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""
from collections import Counter

class Solution:

    def frequencySort(self, s):

        counts = Counter(s) # O(n)
        string_builder = []
        for char, freq in counts.most_common():  # O(k log k) , k for keys
            string_builder.append(char * freq)   # O(n)

        return "".join(string_builder)

        ## Time Complexity: O(n log n)
        ## space Complexity: O(n) for bhashmap and string builder

    def frequencySort_bucketSort(self, s):
        if not s: return s
        counts = Counter(s) # O(n)

        max_freq = max(counts.values())

        buckets = [[] for _ in range(max_freq+1)]
        for c, i in counts.items():
            buckets[i].append(c)   # O(k)

        string_builder = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c*i)  # O(n)

        return "".join(string_builder)

        # Time Complexity: O(n)
        # Space Complexity: O(n)



