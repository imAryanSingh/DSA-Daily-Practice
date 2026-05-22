"""
Problem : Two Sum
Source  : LeetCode #1
Topic   : HashMap / Arrays
Difficulty: Easy
Date    : 2026-05-22

Approach:
  Store each number's index in a hashmap.
  For each element, check if (target - num) already exists.

Time  : O(n)
Space : O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

"""This is My Solution Using Array Approach TC n^2"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
        
