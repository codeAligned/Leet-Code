'''
P-146 - LRU Cache

Design and implement a data structure for Least Recently Used (LRU)
cache. It should support the following operations:getandset. get(key)-
Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.set(key, value)- Set or insert the
value if the key is not already present. When the cache reached its
capacity, it should invalidate the least recently used item before
inserting a new item.

Tags: Data Structure
'''

class Cell(object):
    def __init__(self, k, v, t = -1):
        self.k = k
        self.v = v
        self.t = t

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.now = 0
        self.cap = capacity
        self.bkt = {}
        self.mem = {}

    # Move the cache cell from the old bucket to the new bucket
    def touch(self, cell):
        old, cell.t = cell.t, self.now
        self.now += 1
        if old in self.bkt:
            self.bkt[old].discard(cell)
            if not len(self.bkt[old]):
                self.bkt.pop(old)
        if cell.t not in self.bkt:
            self.bkt[cell.t] = set()
        self.bkt[cell.t].add(cell)

    # @return an integer
    def get(self, key):
        if key in self.mem:
            self.touch(self.mem[key])
            return self.mem[key].v
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.mem:
            self.touch(self.mem[key])
            self.mem[key].v = value
            return
        if len(self.mem) == self.cap:
            lru = min(self.bkt.keys())
            self.mem.pop(self.bkt[lru].pop().k)
            if not len(self.bkt[lru]):
                self.bkt.pop(lru)
        self.mem[key] = Cell(key, value)
        self.touch(self.mem[key])

c = LRUCache(2)

c.set(2, 1)
c.set(3, 2)
print 3, c.get(3)
print 2, c.get(2)
c.set(4, 3)
print 2, c.get(2)
print 3, c.get(3)
print 4, c.get(4)