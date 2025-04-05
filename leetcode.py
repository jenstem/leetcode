# Find Special Substring of Length K #3456

# You are given a string s and an integer k.

# Determine if there exists a substring of length exactly k in s that satisfies the following conditions:

# The substring consists of only one distinct character (e.g., "aaa" or "bbb").
# If there is a character immediately before the substring, it must be different from the character in the substring.
# If there is a character immediately after the substring, it must also be different from the character in the substring.
# Return true if such a substring exists. Otherwise, return false.

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        l, n = 0, len(s)
        while l < n:
            r = l
            while r < n and s[r] == s[l]:
                r += 1
            if r - l == k:
                return True
            l = r
        return False