# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:33:47 2023

@author: Justin Leighton


217. Contains Duplicate
Easy
10.4K
1.2K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        if len(nums) > 1:
            nums.sort()
            val = nums[0]
            for i in range(1, len(nums)):
                if val == nums[i]:
                    return True
                else:
                    val = nums[i]
        return False