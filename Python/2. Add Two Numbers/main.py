from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        cur = res

        while l1 or l2 or carry:
            # getting values for calculating
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # calculating and adding data to node
            sum = (val1 + val2 + carry)
            carry = sum // 10
            val = sum % 10

            # add new node to the list with current val
            cur.next = ListNode(val)

            # moving to next step
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    res = sol.addTwoNumbers(l1, l2)
    while res:
        print(res.val)
        res = res.next

