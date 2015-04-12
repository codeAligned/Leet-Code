'''
P-142 - Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there
is no cycle, returnnull. Follow up:Can you solve it without using
extra space?

Tags: Linked List, Two Pointers
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        # Like P-141, first determine if there is cycle
        start = slow = fast = head
        while slow or fast:
            if slow:
                slow = slow.next
            if fast:
                fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast and slow is not None:
                break
        else:
            return None
        # If there is one, then the distance between the current slow pointer
        # to the cycle start plus the multiples of the cycle equals to the 
        # distance from the head to the cycle start
        while start != slow:
            start = start.next
            slow = slow.next
        return start