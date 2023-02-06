"""

Difficulty: Easy

Question:
---------

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = set(nums)
        if len(x) < len(nums):
            return True
        return False
