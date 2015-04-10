# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode

    # Heap priority queue based solution
    def mergeKLists(self, lists):
        queue = [(item.val, item) for item in lists if item]
        if len(queue) == 1:
            return queue[0][1]
        elif len(queue) == 0:
            return None
        ret = curr = ListNode(0)
        heapq.heapify(queue)
        curr_min = heapq.heappop(queue)[1]
        while len(queue) > 0:
            while curr_min and (not queue[0][1] or curr_min.val <= queue[0][1].val):
                curr.next = curr = curr_min
                curr_min = curr_min.next
            if curr_min:
                curr_min = heapq.heappushpop(queue, (curr_min.val, curr_min))[1]
            else:
                curr_min = heapq.heappop(queue)[1]
        curr.next = curr_min
        return ret.next

    # Divide and Concquer solution

s = Solution()

from random import random

l = [0]*10
ll = [0]*10
for i in range(10):
    l[i] = [int(random()*100) for k in range(10)]
    l[i].sort()
    ll[i] = ListNode(l[i][0])
    curr = ll[i]
    for k in range(1, 10):
        curr.next = ListNode(l[i][k])
        curr = curr.next

def printll(l):
    p = l
    while p:
        print '%2d->' % p.val,
        p = p.next
    print

ll = [ListNode(1), ListNode(0)]
ll = [ListNode(1)]
ll = []
printll(s.mergeKLists(ll))