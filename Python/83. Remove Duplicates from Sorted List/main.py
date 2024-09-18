from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        head_copy = head
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return head_copy
