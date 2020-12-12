"""
Design and implement a data structure for a compressed string iterator.
The given compressed string will be in the form of each letter followed by a positive integer
representing the number of this letter existing in the original uncompressed string.

Implement the StringIterator class:

next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.


Example 1:

Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
"""

import re
class StringIterator:

    def __init__(self, compressedString):
        self._stack = []
        unique_chars = re.findall(r'\D\d+', compressedString)
        # Reversing because we are putting in stack (which is LIFO)
        for char in unique_chars[::-1]:
            # char[1:] because we may get > 1 digits as well
            self._stack.append((char[0], char[1:]))

    def next(self):
        if not self.hasNext():
            return ' '
        curr_val, count = self._stack.pop()
        # we may have duplicate chars like "L1e2t1"
        count -= 1
        if count:
            # pushing again to the stack to fetch it again
            self._stack.append((curr_val, count))
        return curr_val

    def hasNext(self):
        return bool(self._stack)