"""
Problem : Way Too Long Words
Source   : Codeforces 71A
Topic    : Strings / Implementation
Difficulty: 800
Date     : 2026-05-24

Approach:
  For each word, if its length > 10, abbreviate it as:
    first_letter + str(number_of_middle_letters) + last_letter
    e.g. "internationalization" -> "i18n"
  If length <= 10, print the word as-is.

  Number of middle letters = len(word) - 2
  This is the exact rule used in real i18n / l10n abbreviations.

Time  : O(n * L)  where L is avg word length
Space : O(1)
"""
n = int(input())
for _ in range(n):
    word = input().strip()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)

# Test input:
# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis
#
# Expected output:
# word
# l10n
# i18n
# p43s
