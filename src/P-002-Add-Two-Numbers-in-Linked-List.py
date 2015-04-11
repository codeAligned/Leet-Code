'''
P-002 - Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits
are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Tags: Linked List, Math
'''

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        l3 = ret = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val / 10
            l3.next = l3 = ListNode(val % 10) # first assign l3.next then l3
        return ret.next

from utils import *

cases = [
    Test_case((list_gen([2, 4, 3]), list_gen([5, 6, 4])), list_gen([7, 0, 8])),
    Test_case((list_gen([1, 2, 3]), list_gen([4, 5, 6])), list_gen([5, 7, 9])),
    Test_case((list_gen([1, 2, 3, 4]), list_gen([4, 5, 9])), list_gen([5, 7, 2, 5])),
]

run_cases(Solution().addTwoNumbers, cases)
