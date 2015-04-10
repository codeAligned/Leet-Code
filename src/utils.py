# Utilities for Leet Code

# Testing
class Test_case(object):
    def __init__(self, input, output = None):
        self.input = input
        self.output = output   

def run_cases(func, cases, post = lambda x: x):
    for case in cases:
        print 'Input:', case.input, 'Expected:', case.output,
        output = post(func(*case.input))
        print 'Output:', output 

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ''.join(str(node.val) + ' -> ' for node in list_iter(self)) + 'None'

def list_gen(values):
    head = curr = ListNode(0)
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return head.next

def list_iter(head):
    curr = head
    while curr:
        yield curr
        curr = curr.next