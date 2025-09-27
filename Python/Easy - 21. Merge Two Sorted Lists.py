# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        res = ListNode()
        rp = res

        while list1 or list2:
            if not list1:
                rp.next = list2
                list2 = list2.next
            elif not list2:
                rp.next = list1
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    rp.next = list2
                    list2 = list2.next
                else:
                    rp.next = list1
                    list1 = list1.next
            rp = rp.next

        return res.next
