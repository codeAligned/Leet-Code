'''
P-092 - Reverse Linked List II

Reverse a linked list from positionmton. Do it in-place and in one-
pass. For example:Given1->2->3->4->5->NULL,m= 2 andn= 4,
return1->4->3->2->5->NULL. Note:Givenm,nsatisfy the following
condition:1 mn length of list.

Tags: Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode

    # Solution 1
    def reverseBetween(self, head, m, n):
        ret = prev = ListNode(0)
        ret.next = curr = head
        count = 0
        while count < m - 1:
            prev = curr
            curr = curr.next
            count += 1
        save = prev
        while count < n:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        save.next.next = curr
        save.next = prev
        return ret.next

    def reverseBetween(self, head, m, n):
        ret = curr = ListNode(0)
        ret.next = ptr = head
        # find the (m-1)th node
        count = 0
        while count < m - 1:
            curr.next = ptr
            curr = ptr
            ptr = ptr.next
            count += 1
        # reverse from ptr to the nth node
        prev = curr
        while count < n:
            next = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next
            count += 1
        curr.next.next = ptr
        curr.next = prev
        return ret.next

s = Solution()
l = ListNode(0)
ptr = l
for i in range(1, 6):
    ptr.next = ListNode(i)
    ptr = ptr.next

ptr = l
while ptr:
    print ptr.val, '->',
    ptr = ptr.next
print

n = s.reverseBetween(l, 1, 3)

ptr = n
while ptr:
    print ptr.val, '->',
    ptr = ptr.next
print