# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def traverse(node):
            if node:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return result