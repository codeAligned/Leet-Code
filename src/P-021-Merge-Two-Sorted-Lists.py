'''
P-021 - Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new
list should be made by splicing together the nodes of the first two
lists.

Tags: Linked List
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        # Dummy head
        ret = curr = ListNode(0)
        while l1 or l2:
            while l1 and (not l2 or l1.val <= l2.val):
                curr.next = curr = l1 # ==> curr.next = l1 THEN curr = l1
                l1 = l1.next
            l1, l2 = l2, l1 # swap so we can eliminate one while loop
        return ret.next

s = Solution()

l1 = None
l2 = ListNode(0)

l3 = s.mergeTwoLists(l1, l2)
p = l3
while p:
    print p.val,
    print '->'
    p = p.next
print
