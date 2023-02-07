"""
Difficulty: Medium

Description:
------------

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example:
--------
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        output[0] = 1*nums[1]*nums[2]*...*nums[n-1]
        output[1] = nums[0]*1*nums[2]*...*nums[n-1]
        ...
        output[n-1] = nums[0]*nums[1]*...*nums[n-2]

        output[i] = (product of numbers before i) x (product of numbers after  )
        """
        before = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            before[i] = before[i-1]*nums[i-1]

        after = [1 for i in range(len(nums))]

        for j in range(len(nums)-2,-1,-1):
            after[j] = after[j+1]*nums[j+1]
        
        return [before[i]*after[i] for i in range(len(nums))]
