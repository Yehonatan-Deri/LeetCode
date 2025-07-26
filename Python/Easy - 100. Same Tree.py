# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    # Run-time O(n)
    # Space complexity 0(1)
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # if at the ends its the same then its the same
        if p is None and q is None:
            return True
        # if one of them is not the same then end the recursion and return false
        if (p is None or q is None) or (p.val != q.val):
            return False

        # check both left and right sides
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
