"""
Difficulty: Medium

Question:
---------
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Examples:
---------
Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]

Example 2:
    Input: nums = [0,1,1]
    Output: []

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
"""

# 2 SOLUTIONS -- FIRST ONE IS SLOWER BUT SIMPLER

# Solution 1

class Solution:
    def twoSum(self,subnums, tgt):
        acc = []
        diff = {}
        for i in range(len(subnums)):
            difference = tgt - subnums[i]
            if subnums[i] in diff:
                acc.append([subnums[i], diff[subnums[i]]])
            else:
                diff[difference] = subnums[i]
        return acc 
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rval = set()
        # for each element
        for i in range(len(nums)-1):
            # compute 2 sum on -ve value (need 0 sum)
            tmp = self.twoSum(nums[i+1:],-nums[i])
            if len(tmp) != 0:
                for l in tmp:
                    # since sorted and using set, duplicates taken care of 
                    rval.add(tuple(l) + (nums[i],))

        return list(rval)

# Faster solution 

# Solution 2

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        rval = set()
       
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # if sum to 0 
                if total == 0:
                    # add to set -- no need to worry about duplicates (sorted)
                    rval.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                # if < 0, need larger numbers
                if total < 0:
                    j += 1
                # if > 0, need lower numbers
                if total > 0:
                    k -= 1


        return list(rval)



