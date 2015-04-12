'''
P-147 - Insertion Sort List

Sort a linked list using insertion sort.

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
    def insertionSortList(self, head):
        curr = prev = ret = ListNode(0)
        ret.next = head
        while curr.next:
            # if the curr value is greater than the 
            # previously inserted node, we don't have to go 
            # back to the beginning.
            # otherwise we need to start searching from the begining
            if prev.next.val > curr.next.val:
                prev = ret
            while prev.next.val < curr.next.val:
                prev = prev.next
            if prev != curr:
                node = curr.next
                curr.next = node.next
                node.next = prev.next
                prev.next = node
            else:
                curr = curr.next
        return ret.next

    def print_list(self, head):
        ptr = head
        while ptr:
            print ptr.val, '->',
            ptr = ptr.next
        print

s = Solution()
l = ListNode(1)
l.next = ListNode(3)
l.next.next = ListNode(2)
l.next.next.next = ListNode(5)
l.next.next.next.next = ListNode(0)

l = s.insertionSortList(l)
s.print_list(l)