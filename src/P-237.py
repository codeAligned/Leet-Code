# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        curr = node
        
        while curr.next:
            # Shifting the values
            curr.val = curr.next.val
            
            # If I am the second last element - unlink the last one
            if not curr.next.next:
                curr.next = None
            # Else continue to the next one
            else:
                curr = curr.next