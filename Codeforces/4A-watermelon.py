"""
Problem : Watermelon
Source  : Codeforces 4A
Topic   : Math / Parity
Difficulty: 800 (CF Rating)
Date    : 2026-05-22

Approach:
  A watermelon of weight W must be split into two even parts.
  Condition: W must be even AND W > 2.
  (W=2 fails because only split is 1+1, both odd)

Time  : O(1)
Space : O(1)
"""

w = int(input())
if w % 2 == 0 and w > 2:
    print("YES")
else:
    print("NO")
