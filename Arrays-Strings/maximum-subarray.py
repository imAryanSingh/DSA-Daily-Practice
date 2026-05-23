# Problem : Maximum Subarray
# Source   : LeetCode #53  |  Striver A2Z — Step 3 Arrays
# Topic    : Kadane's Algorithm / Dynamic Programming
# Difficulty: Medium
# Date     : 2026-05-23
#
# Approach (Kadane's Algorithm):
#   Maintain two variables:
#     current_sum — the maximum subarray sum ending at this index
#     max_sum     — the global maximum seen so far
#
#   At each element:
#     current_sum = max(num, current_sum + num)
#       (either start a new subarray here, or extend the previous one)
#     max_sum = max(max_sum, current_sum)
#
#   Key insight: if current_sum ever goes negative, it will only hurt
#   any future subarray — so reset it by starting fresh at current element.
#
# Time  : O(n)
# Space : O(1)

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


# ── Test cases ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6  ([4,-1,2,1])
    print(sol.maxSubArray([1]))                                 # 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                   # 23
    print(sol.maxSubArray([-1, -2, -3]))                        # -1 (all negative)
