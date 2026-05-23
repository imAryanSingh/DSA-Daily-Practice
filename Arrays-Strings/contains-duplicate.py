# Problem : Contains Duplicate
# Source   : LeetCode #217
# Topic    : HashMap / Arrays
# Difficulty: Easy
# Date     : 2026-05-23
#
# Approach:
#   Add each number to a set as we iterate.
#   If the number already exists in the set, a duplicate is found — return True.
#   If we finish the loop without finding one, return False.
#
# Time  : O(n)
# Space : O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() # 1 set do not have duplicates
        for num in nums:
            if num in seen: # 3 seen me kya vo number hai
                return True 
            seen.add(num) # 2 num ko add kiya seen me 
        return False


# ── Test cases ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))   # True
    print(sol.containsDuplicate([1, 2, 3, 4]))   # False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
