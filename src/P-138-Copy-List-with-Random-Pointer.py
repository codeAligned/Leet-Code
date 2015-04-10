# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode

    def factory():
        return RandomListNode(0)

    # One-pass Solution using defaultdict
    def copyRandomList(self, head):
        if not head:
            return None
        temp = head
        node_map = collections.defaultdict(self.factory)
        node_map[None] = None # avoid None as key to generate a RandomListNode
        while temp:
            node_map[temp].label = temp.label
            node_map[temp].next = node_map[temp.next]
            node_map[temp].random = node_map[temp.random]
            temp = temp.next
        del node_map[None]
        return node_map[head]

    # Two-pass Solution - simple
    def copyRandomList(self, head):
        curr = head
        node_map = {None: None}
        while curr:
            node_map[curr] = RandomListNode(curr.label)
            curr = curr.next
        curr = head
        while curr:
            node_map[curr].next = node_map[curr.next]
            node_map[curr].random = node_map[curr.random]
            curr = curr.next
        return node_map[head]