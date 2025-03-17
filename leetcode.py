# Base 7 #504

# Given an integer num, return a string of its base 7 representation.

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"
 
# Constraints:

# -107 <= num <= 107

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            return '-' + self.convertToBase7(-num)
        ans = []
        while num:
            ans.append(str(num % 7))
            num //= 7
        return ''.join(ans[::-1])