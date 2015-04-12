'''
P-160 - Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two
singly linked lists begins. For example, the following two linked
lists: begin to intersect at node c1. Notes:If the two linked lists
have no intersection at all, returnnull.The linked lists must retain
their original structure after the function returns.You may assume
there are no cycles anywhere in the entire linked structure.Your code
should preferably run in O(n) time and use only O(1) memory.
Credits:Special thanks to@stellarifor adding this problem and creating
all test cases.

Tags: Linked List
'''

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