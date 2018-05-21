# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1 or not self.isBalanced(root.right) or not self.isBalanced(root.left):
            return False

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

