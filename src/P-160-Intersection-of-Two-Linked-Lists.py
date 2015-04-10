# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        ptr1, ptr2 = headA, headB
        if ptr1 == None or ptr2 == None:
            return None
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
            if ptr1 == ptr2:
                return ptr1
            if ptr1 == None:
                ptr1 = headB
            if ptr2 == None:
                ptr2 = headA
        return ptr1