'''
P-025 - Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked listkat a time and
return its modified list. If the number of nodes is not a multiple
ofkthen left-out nodes in the end should remain as it is. You may not
alter the values in the nodes, only nodes itself may be changed. Only
constant memory is allowed. For example,Given this linked
list:1->2->3->4->5 Fork= 2, you should return:2->1->4->3->5 Fork= 3,
you should return:3->2->1->4->5

Tags: Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        ret = prev = ListNode(0)
        ret.next = head
        cnt = 1
        while head:
            if cnt == k:
                cnt = 1
                next = head.next
                self.reverseList(prev.next, head)
                prev.next, prev, head = head, prev.next, next
            else:
                cnt += 1
                head = head.next
        return ret.next

    # Reverse the list from start to end in place 
    # return the new start of the reversed list
    def reverseList(self, start, end):
        curr, prev = start, end.next
        while prev != end:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        
s = Solution()

head = ListNode(0)
ptr = head
for i in range(1, 10):
    ptr.next = ListNode(i)
    if i == 6:
        t = ptr
    ptr = ptr.next

def printll(l):
    p = l
    while p:
        print '%2d->' % p.val,
        p = p.next
    print

printll(head)
printll(s.reverseKGroup(head, 3))