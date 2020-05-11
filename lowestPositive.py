"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

from __init__ import duration
import unittest


class Solution():

    @staticmethod
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @duration
    def better(self, nums) -> int:
        # If empty array or doesn't have 1, return 1
        if not next((x for x in nums if x == 1), 0):
            return 1

        lo: int = 0
        hi: int = len(nums) - 1
        i: int = 0
        pivot: int = 1 # minimum value will be 1 , taking it as pivot

        while i <= hi:
            if nums[i] < pivot:    # all the zeros and negatives
                self.swap(nums, i, hi)  # pushing all negatives and zeros to right
                hi -= 1
            elif nums[i] > pivot:   # skipping doing anything if number is positive
                i += 1
                lo += 1
            else:
                i += 1
        x = 0
        while x <= hi:            # last index of all the positive numbers will be hi
            y = abs(nums[x])
            if 0 < y <= hi+1 and nums[y-1] > 0:
                nums[y-1] *= -1
            x+=1
        return next((i for i, v in enumerate(nums[:hi + 1]) if v >= 0), x) + 1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = [3, 4, -1, 1]
        self.input2 = [1, 2, 0]
        self.input3 = [1,-1,-5,-3,3,4,2,8]
        self.obj = Solution()

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res, 2)
        res = self.obj.better(self.input2)
        self.assertEqual(res, 3)
        res = self.obj.better(self.input3)
        self.assertEqual(res, 5)


if __name__ == '__main__':
        unittest.main()




