"""
Next Round
Problem : Next Round
Source   : Codeforces 158A
Topic    : Sorting / Implementation
Difficulty: 800
Date     : 2026-05-25

Problem summary:
  n participants scored points. Top k advance.
  But if the k-th participant has the same score as k+1, k+2... they
  also advance (no one is eliminated mid-tie).
  Count how many participants advance.

Approach:
  Read scores (already sorted descending in the problem, but verify).
  The cutoff score is scores[k-1] (0-indexed).
  Count all participants whose score >= cutoff AND score > 0.
  (Score of 0 never advances regardless of tie.)

Time  : O(n)
Space : O(1)
"""

n, k = map(int, input().split())
scores = list(map(int, input().split()))

cutoff = scores[k - 1]
count = 0
for s in scores:
    if s >= cutoff and s > 0:
        count += 1

print(count)

# Test input:
# 8 5
# 10 9 8 7 7 7 5 5
# Expected: 6   (cutoff=7, three people tied at 7 all advance)

# Edge case:
# 5 3
# 5 4 0 0 0
# Expected: 2   (cutoff=0 but score=0 never advances)
