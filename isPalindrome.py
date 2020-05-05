from __init__ import duration
import unittest

class Solution:
    # @param A : string
    # @return an integer

    # intuitive
    @duration
    def intuitive(self, A):
        from_left = ''
        from_right = ''
        possible_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for i in range(len(A)):
            if A[i].lower() not in possible_chars.lower():
                continue
            from_left += A[i]
        for i in range(len(A)-1, -1, -1):
            if A[i].lower() not in possible_chars.lower():
                continue
            from_right += A[i]
        if from_left.lower() == from_right.lower():
            return 1
        return 0

    # Better
    @duration
    def better(self, A):
        start = 0
        end = len(A)-1
        if not A:
            return 1
        while start < end :
            if A[start].isalnum() and A[end].isalnum():
                start_string = A[start].lower()
                end_string = A[end].lower()
                if start_string != end_string:
                    return 0
                else:
                    start +=1
                    end -=1
            elif not A[start].isalnum():
                start +=1
            elif not A[end].isalnum():
                end -=1
        return 1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = "A man, a plan, a canal: Panama"
        self.input2 = "race a car"
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res, 1)
        res = self.obj.intuitive(self.input2)
        self.assertEqual(res, 0)

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res, 1)
        res = self.obj.better(self.input2)
        self.assertEqual(res, 0)


if __name__ == '__main__':
        unittest.main()




