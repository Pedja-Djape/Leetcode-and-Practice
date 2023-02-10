"""
Difficulty: Medium

Description:
------------
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.


Example:
--------
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Constraints:
1 <= nums.length <= 10^5 
-10^4 <= nums[i] <= 10^4
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # return max_sum
        max_sum = nums[0]
        # the current sum of the sub array
        running_sum = 0
        for i in range(len(nums)):
            # if the number is negative it isn't contributing to the max sum
            if running_sum < 0:
                running_sum = 0
            # increase sum by current value
            running_sum += nums[i]

            max_sum = max(max_sum,running_sum)
        return max_sum
        

                