# Two Out of Three #2032

# Given three integer arrays nums1, nums2, and nums3, return a distinct array 
# containing all the values that are present in at least two out of the three 
# arrays. You may return the values in any order.

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return [i for i in range(1, 101) if (i in s1) + (i in s2) + (i in s3) > 1]