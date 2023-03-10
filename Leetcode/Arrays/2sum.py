"""

Difficulty: Easy

Question:
---------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
--------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need some memory store to track values already seen
        seen = {} # tracks difference between elements in nums and target

        for i,v in enumerate(nums):
            if v in seen:
                return [seen[v],i]
            else:
                # target = v + other_v
                # target - v = other_v
                seen[target - v] = i
