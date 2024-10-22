# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def depth_first(root, s):
            if root is None:
                return False
            s += root.val
            if root.left is None and root.right is None and s == targetSum:
                return True
            return depth_first(root.left, s) or depth_first(root.right, s)

        return depth_first(root, 0)