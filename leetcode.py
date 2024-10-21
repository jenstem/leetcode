# Given an integer array nums where the elements are sorted in ascending order, convert it to a
# height-balanced binary search tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def convertToBST(left, right):
            if left > right:
                return None
            mid = (left + right) >> 1
            left = convertToBST(left, mid - 1)
            right = convertToBST(mid + 1, right)
            return TreeNode(nums[mid], left, right)

        return convertToBST(0, len(nums) - 1)