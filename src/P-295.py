from heapq import *

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # lq - max-heap for the left half
        # rq - min-heap for the right half
        self.lq, self.rq = [], []
        
    def balance(self):
        
        # Make sure the length differs by up to 1
        
        while len(self.lq) > len(self.rq) + 1:
            num = -heappop(self.lq)
            heappush(self.rq, num)
            
        while len(self.rq) > len(self.lq) + 1:
            num = heappop(self.rq)
            heappush(self.lq, -num)

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        
        if not self.lq or num <= -self.lq[0]:
            heappush(self.lq, -num)
        else:
            heappush(self.rq, num)
        
        self.balance()

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.lq) > len(self.rq):
            return -self.lq[0]
        elif len(self.lq) < len(self.rq):
            return self.rq[0]
        else:
            return (-self.lq[0] + self.rq[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()