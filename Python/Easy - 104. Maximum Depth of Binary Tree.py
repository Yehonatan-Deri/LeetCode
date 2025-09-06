# Definition for a binary tree node.
from numpy.ma.core import left_shift


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        return self.calcDepth(root.left, root.right, 1)

    def calcDepth(self, l, r, depth):
        if r is None and l is None:
            return depth
        elif r and not l:
            return self.calcDepth(r.left, r.right, depth + 1)
        elif l and not r:
            return self.calcDepth(l.left, l.right, depth + 1)

        return max(self.calcDepth(l.left, l.right, depth + 1), self.calcDepth(r.left, r.right, depth + 1))

    #### another way
    # def maxDepth(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #     left = self.maxDepth(root.left)
    #     right = self.maxDepth(root.right)
    #     return 1 + max(left, right)
    ###