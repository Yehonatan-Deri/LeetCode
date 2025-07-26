# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Runtime O(n)
    # Space Complexity O(1)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # if empty
        if root is None:
            return True
        return self.checkSymetric(root.left, root.right)

    def checkSymetric(self, l, r):
        # if both null its same
        if l is None and r is None:
            return True
        # if one is missing or different value its not the same
        if (l is None or r is None) or (l.val != r.val):
            return False

        return self.checkSymetric(l.left, r.right) and self.checkSymetric(l.right, r.left)
