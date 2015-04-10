# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        # dummy heads
        lhead = lcurr = ListNode(0)
        hhead = hcurr = ListNode(0)
        curr = head
        while curr:
            if curr.val < x:
                lcurr.next = curr
                lcurr = curr
            else:
                hcurr.next = curr
                hcurr = curr
            curr = curr.next
        if not lhead.next:
            return hhead.next
        else:
            lcurr.next = hhead.next
            if hcurr:
                hcurr.next = None
            return lhead.next

s = Solution()
l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(2)

n = s.partition(l, 4)
ptr = n
while ptr:
    print ptr.val,'->',
    ptr = ptr.next
print
