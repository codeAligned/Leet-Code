# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        ret = prev = ListNode(0)
        ret.next = curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next
            curr = curr.next
        return ret.next

s = Solution()
l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(1)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(3)
l.next.next.next.next.next = ListNode(3)
l.next.next.next.next.next.next = ListNode(3)

n = s.deleteDuplicates(l)
ptr = n
print 'result'
while ptr:
    print ptr.val,'->',
    ptr = ptr.next
print