# Definition for singly-linked list.
from numpy.lib.polynomial import roots


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1, p2 = head, head

        # if there is a next so p2 wont throw null exception
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

        return False


if __name__ == '__main__':
    sol = Solution()

    # print(sol.hasCycle())
