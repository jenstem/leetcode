# Find Numbers with Even Number of Digits #1295

# Given an array nums of integers, return how many of 
# them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(abs(num))) % 2 == 0)