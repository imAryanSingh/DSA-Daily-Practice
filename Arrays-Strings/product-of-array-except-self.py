"""
Product of Array Except Self
Problem : Product of Array Except Self
Source   : LeetCode #238  |  NeetCode 150 — Arrays & Hashing
Topic    : Prefix Product / Arrays
Difficulty: Medium
Date     : 2026-05-25

Approach:
  Build a prefix product array (left pass):
    prefix[i] = product of all elements to the LEFT of i
  Then do a right pass multiplying suffix product on the fly:
    result[i] = prefix[i] * suffix_running_product

  No division allowed (constraint). No extra array for suffix needed —
  use a single variable and update result in-place from right to left.

  Example: nums = [1, 2, 3, 4]
    After left pass:  result = [1, 1, 2, 6]
    Right pass (suffix running = 1):
      i=3: result[3] = 6*1=6,  suffix=4
      i=2: result[2] = 2*4=8,  suffix=12
      i=1: result[1] = 1*12=12, suffix=24
      i=0: result[0] = 1*24=24, suffix=24
    Final: [24, 12, 8, 6]

Time  : O(n)
Space : O(1)  — output array does not count as extra space
"""


class Solution:
    def productExceptSelf(self, nums):
        result = [1] * n

        # Left pass — prefix products
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # Right pass — multiply suffix products in-place
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

# Test cases
# productExceptSelf([1,2,3,4])   -> [24,12,8,6]
# productExceptSelf([-1,1,0,-3,3]) -> [0,-3,9,0,0]
