'''
P-083 - Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each
element appear onlyonce. For example,Given1->1->2,
return1->2.Given1->1->2->3->3, return1->2->3.

Tags: Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        ret = slow = head
        if head:
            fast = head.next
            while fast:
                if fast.val != slow.val:
                    slow.next = fast
                    slow = slow.next
                else:
                    slow.next = None
                fast = fast.next
        return ret

s = Solution()

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(3)

rl = s.deleteDuplicates(l)
while rl:
    print rl.val,'->',
    rl = rl.next
print