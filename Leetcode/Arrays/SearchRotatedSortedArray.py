"""
Search in Rotated Sorted Array

Difficulty: Medium 

Question:
--------
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example(s):
--------

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        
        l = 0
        r = len(nums) - 1

        while l < r:
            # checking ptrs
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if l == r - 1:
                return -1
            # if left ptr < mid ptr
            if nums[l] < nums[m]:
                # if target within left bound, shift right ptr
                if target > nums[l] and target < nums[m]:
                    r = m
                    continue
                if target > nums[m] or target < nums[l]:
                    l = m
                    continue
            if nums[l] > nums[m]:
                if target < nums[m] or nums[l] < target:
                    r = m
                    continue

            if nums[m] < nums[r]:
                if target > nums[m] and target < nums[r]:
                    l = m
                    continue
                if target < nums[m] or target > nums[r]:
                    r = m
            
            if nums[m] > nums[r]:
                if target < nums[r] or nums[m] < target:
                    l = m
                    continue
            
            
        return -1