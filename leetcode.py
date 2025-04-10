# Final Array State After K Multiplication Operations 1 #3264


# You are given an integer array nums, an integer k, and an integer multiplier.

# You need to perform k operations on nums. In each operation:

# Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# Return an integer array denoting the final state of nums after performing all k operations.

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
            for _ in range(k):
                min_index = nums.index(min(nums))
                nums[min_index] = nums[min_index] * multiplier
            return nums  