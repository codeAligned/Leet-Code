'''
P-061 - Rotate List

Given a list, rotate the list to the right bykplaces, wherekis non-
negative. For
example:Given1->2->3->4->5->NULLandk=2,return4->5->1->2->3->NULL.

Tags: Linked List, Two Pointers
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head:
            return head

        length = count = 1
        tail = prev = head

        # Get the length and the tail
        while tail.next:
            length += 1
            tail = tail.next

        # Find the end after rotation
        # Only iterate less than the length
        while count < length - k % length:
            prev = prev.next
            count += 1

        node = prev.next if prev.next else head
        tail.next = head
        prev.next = None

        return node

# Testing
from utils import *

cases = [
    Test_case((list_gen(range(1, 5)), 1), list_gen([4,1,2,3,])),
    Test_case((list_gen(range(1, 5)), 2), list_gen([3,4,1,2,])),
    Test_case((list_gen(range(1, 5)), 3), list_gen([2,3,4,1,])),
    Test_case((list_gen(range(1, 5)), 4), list_gen([1,2,3,4,])),
    Test_case((list_gen(range(1, 5)), 5), list_gen([4,1,2,3,])),
]
run_cases(Solution().rotateRight, cases)