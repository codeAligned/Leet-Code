# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr:
            
            # Need to remove
            if curr.val == val:
                # Not the head of the list
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            # No need to remove
            else:
                prev = curr
            
            # Move to the next node    
            curr = curr.next
                
        return head