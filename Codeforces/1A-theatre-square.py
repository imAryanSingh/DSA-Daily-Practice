# Problem : Theatre Square
# Source   : Codeforces Round 1 — Problem 1A
# Topic    : Math / Ceiling Division
# Difficulty: 800 (Div 2 A)
# Date     : 2026-05-23
#
# Problem statement (summary):
#   A rectangular theatre square of size n x m metres must be paved
#   with square flagstones of size a x a metres.
#   Flagstones may not be cut. Find the minimum number of flagstones needed.
#
# Approach:
#   Along the n-direction we need ceil(n / a) flagstones.
#   Along the m-direction we need ceil(m / a) flagstones.
#   Total = ceil(n/a) * ceil(m/a)
#
#   Ceiling division without importing math:
#     ceil(x / a) = (x + a - 1) // a   (integer arithmetic trick)
#
#   Why this works: adding (a-1) before floor division "rounds up" any
#   remainder, which is exactly what ceiling does.
#
# Time  : O(1)
# Space : O(1)

import math

def solve():
    n, m, a = map(int, input().split())
    rows = math.ceil(n / a)
    cols = math.ceil(m / a)
    print(rows * cols)

solve()


# ── Manual test (comment out solve() above to use) ──────────────────────────
# def test():
#     cases = [(6, 6, 4), (1, 1, 1), (4, 4, 2), (5, 5, 3)]
#     # Expected:  4,         1,         4,         4
#     for n, m, a in cases:
#         ans = math.ceil(n/a) * math.ceil(m/a)
#         print(f"n={n} m={m} a={a} -> {ans}")
# test()
