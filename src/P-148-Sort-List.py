'''
P-148 - Sort List

Sort a linked list inO(nlogn) time using constant space complexity.

Tags: Linked List, Sort
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    # Mergesort-based Solution
    def merge(self, l1, l2):
        ret = curr = ListNode(0)
        while l1 or l2:
            while l1 and (not l2 or l1.val <= l2.val):
                curr.next = curr = l1 # ==> curr.next = l1 THEN curr = l1
                l1 = l1.next
            l1, l2 = l2, l1 # swap so we can eliminate one while loop
        return ret.next

    def split(self, head):
        slow = fast = ret = ListNode(0)
        ret.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        next = slow.next
        slow.next = None
        return head, next

    def sortList(self, head):
        if not head or not head.next:
            return head
        else:
            s1, s2 = self.split(head)
            l1 = self.sortList(s1)
            l2 = self.sortList(s2)
            return self.merge(l1, l2)

    def print_list(self, head, tail = None):
        ptr = head
        while ptr != tail:
            print ptr.val, '->',
            ptr = ptr.next
        print

s = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(2)
l.next.next.next = ListNode(5)
l.next.next.next.next = ListNode(0)

l = s.sortList(l)
s.print_list(l)