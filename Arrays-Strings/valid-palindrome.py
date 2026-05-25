"""
Problem : Valid Palindrome
Source   : LeetCode #125  |  NeetCode 150 — Two Pointers
Topic    : Two Pointers / Strings
Difficulty: Easy
Date     : 2026-05-25

Approach:
  Use two pointers — left starting at 0, right starting at end.
  Skip any character that is not alphanumeric (isalnum()).
  Compare lowercased characters at both pointers.
  If they differ at any point, return False.
  Pointers move inward until they meet.

  Why two pointers: avoids creating a cleaned string (O(n) space).
  Doing it in-place is the interviewer-preferred approach.

Time  : O(n)
Space : O(1)
"""

# My Solution 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for char in s:
            if char.isalnum():
                string=string+char.lower()
        if string[::-1]==string:
            return True
        return False



class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# Test cases
# isPalindrome("A man, a plan, a canal: Panama") -> True
# isPalindrome("race a car")                     -> False
# isPalindrome(" ")                              -> True  (empty after clean)
