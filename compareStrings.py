"""
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""
from __init__ import duration
import unittest


class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    @duration
    def intuitive(self, A, B):
        lA = list(map(int, A.split('.')))
        x = len(lA)
        lB = list(map(int, B.split('.')))
        y = len(lB)
        while x > y:
            lB.append(0)
            y+=1
        while y > x:
            lA.append(0)
            x+=1
        if lA>lB:
            return 1
        if lB>lA:
            return -1
        return 0

    @duration
    def faster(self, A, B):
        lA = A.split('.')
        lB = B.split('.')
        for i in range(len(lA)-1, -1, -1):
            if int(lA[i]) == 0:
                lA.pop()
            else:
                break
        for i in range(len(lB)-1, -1, -1):
            if int(lB[i]) == 0:
                lB.pop()
            else:
                break
        for i in range(0, min(len(lA), len(lB))):
            if int(lA[i]) > int(lB[i]):
                return 1
            elif int(lA[i]) < int(lB[i]):
                return -1
        if len(lA) == len(lB):
            return 0
        else:
            if len(lA) > len(lB):
                return 1
            else:
                return -1

class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.A1, self.B1 = '13.0', '13.0.4'
        self.A2, self.B2 = '01', '1'
        self.A3, self.B3 = '1.1', '1.1.0'
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.A1, self.B1)
        self.assertEqual(res, -1)
        res = self.obj.intuitive(self.A2, self.B2)
        self.assertEqual(res, 0)
        res = self.obj.intuitive(self.A3, self.B3)
        self.assertEqual(res, 0)

    def test_better(self):
        res = self.obj.better(self.A1, self.B1)
        self.assertEqual(res, -1)
        res = self.obj.better(self.A2, self.B2)
        self.assertEqual(res, 0)
        res = self.obj.better(self.A3, self.B3)
        self.assertEqual(res, 0)


if __name__ == '__main__':
        unittest.main()