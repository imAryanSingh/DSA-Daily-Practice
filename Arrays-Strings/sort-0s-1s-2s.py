"""
Problem : Sort an Array of 0s, 1s and 2s
Source  : LeetCode #75 (Sort Colors)
Topic   : Dutch National Flag / Arrays
Difficulty: Medium
Date    : 2026-05-22

Approach:
  Three pointers — low, mid, high.
  - Swap nums[mid] with nums[low], advance both if nums[mid] == 0
  - Just advance mid if nums[mid] == 1
  - Swap nums[mid] with nums[high], decrement high if nums[mid] == 2
  Loop until mid > high.

Time  : O(n)
Space : O(1)
"""
class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
              
"""This is my approach I thought to simply sort them O(nlogn)"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(nums.sort())
