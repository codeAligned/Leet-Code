# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        ret = curr = ListNode(0)
        ptr = head
        while ptr and ptr.next:
            curr.next = ptr.next
            ptr.next = ptr.next.next
            curr.next.next = ptr
            # now ptr is the second element
            curr = ptr
            ptr = ptr.next
        if ptr:
            curr.next = ptr
        return ret.next

s = Solution()

head = ListNode(0)
ptr = head
for i in range(1, 10):
    ptr.next = ListNode(i)
    ptr = ptr.next

def printll(l):
    p = l
    while p:
        print '%2d->' % p.val,
        p = p.next
    print

printll(head)
printll(s.swapPairs(head))