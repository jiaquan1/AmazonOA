"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
import collections
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        d=collections.defaultdict(lambda:Node(0,None,None))
        d[None]=None
        m=head
        while m:
            d[m].val=m.val
            d[m].next=d[m.next]
            d[m].random=d[m.random]
            m=m.next
        return d[head]

        




