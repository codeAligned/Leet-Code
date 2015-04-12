'''
P-143 - Reorder List

Given a singly linked listL:L0L1Ln-1Ln,reorder it to:L0LnL1Ln-1L2Ln-2
You must do this in-place without altering the nodes' values. For
example,Given{1,2,3,4}, reorder it to{1,4,2,3}.

Tags: Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def _splitList(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        fast = fast.next
    middle = slow.next
    slow.next = None

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):
  last = None
  currentNode = head

  while currentNode:
    nextNode = currentNode.next
    currentNode.next = last
    last = currentNode
    currentNode = nextNode

  return last

# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):
    tail = head = a
    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a
    return head

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return
        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)

    def print_list(self, head):
        ptr = head
        while ptr:
            print ptr.val, '->',
            ptr = ptr.next
        print

s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s.reorderList(l)
s.print_list(l)