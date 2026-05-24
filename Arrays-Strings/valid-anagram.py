"""
Problem : Valid Anagram
Source   : LeetCode #242
Topic    : HashMap / Strings
Difficulty: Easy
Date     : 2026-05-24

Approach:
  Count frequency of each character in string s using a hashmap.
  Decrement the count for each character in string t.
  If any count goes non-zero at the end, they are not anagrams.
  Early exit: if len(s) != len(t), return False immediately.

Time  : O(n)
Space : O(1)  — at most 26 keys (lowercase English letters)
"""
#Best Approach
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

# Claude Approach Using Hashmap
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            count[ch] = count.get(ch, 0) - 1
            if count[ch] < 0:
                return False
        return True

# My Approach 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for char in s:
            if s.count(char)!=t.count(char):
                return False
        return True

        

# Test cases
# isAnagram("anagram", "nagaram")  -> True
# isAnagram("rat", "car")          -> False
# isAnagram("a", "ab")             -> False
