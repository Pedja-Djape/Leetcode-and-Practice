"""
Difficulty: Medium

Question:
---------
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example:
--------
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [6,1,2,3,4,5]
        """

        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]

        while (l < r):
            if l == r - 1:
                return min(nums[l],nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            m = (l + r) // 2
            if nums[m] > nums[l]:
                l = m
                continue
            if nums[m] < nums[r]:
                r = m
                continue
            