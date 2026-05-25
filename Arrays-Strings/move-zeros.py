"""
Problem : Move Zeroes
Source   : LeetCode #283  |  Striver A2Z — Step 3 Arrays
Topic    : Two Pointers / In-place
Difficulty: Easy
Date     : 2026-05-25

Approach:
  Use a slow pointer (insert_pos) that tracks where the next
  non-zero element should go.
  Fast pointer (i) scans the whole array.
  When nums[i] != 0, place it at insert_pos and advance insert_pos.
  After the loop, fill everything from insert_pos to end with 0.

  Key insight: this is the same partition idea as Dutch National Flag
  but simpler — just two groups (non-zero | zero).

  Do it in-place, minimum operations — don't use extra array.

Time  : O(n)
Space : O(1)
"""
class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0

        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill remaining positions with zero
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

# Test cases
# nums = [0,1,0,3,12] -> [1,3,12,0,0]
# nums = [0]          -> [0]
# nums = [1,0,0,3,0]  -> [1,3,0,0,0]
