# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        cnt = 0
        curr, prev = head, None
        while curr:
            if cnt == n:
                prev = head
            elif cnt > n:
                prev = prev.next
            curr = curr.next
            cnt += 1
        if prev:
            prev.next = prev.next.next
            return head
        else:
            return head.next

s = Solution()

for i in range(1, 6):
    l = ListNode(1)
    ptr = l
    for k in range(2, 6):
        ptr.next = ListNode(k)
        ptr = ptr.next
    ptr = s.removeNthFromEnd(l, i)
    while ptr != None:
        print ptr.val,
        ptr = ptr.next
    print