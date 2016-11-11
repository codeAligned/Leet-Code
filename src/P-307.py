from math import ceil, log

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        if nums:
            level = int(ceil(log(len(nums), 2)) + 1)
        else:
            level = 1
        self.level = level

        self.A = [0] * (2 ** level)

        for i, n in enumerate(self.nums):
            self.A[2 ** (level - 1) + i] = n

        for i in reversed(range(level - 1)):
            for j in range(2 ** i):
                index = 2 ** i + j
                self.A[index] = self.A[2 * index] + self.A[2 * index + 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        
        index = 2 ** (self.level - 1) + i
        while index > 0:
            self.A[index] += delta
            index /= 2

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        left, right = self.sum_up_to(i), self.sum_up_to(j)

        return right - left + self.nums[i]

    def sum_up_to(self, i):
        curr = 1
        left = self.A[1]
        binary = '0' * (self.level - 1 - len(bin(i)[2:])) + bin(i)[2:]
        for c in binary:
            if c == '0':
                curr = curr * 2
                if curr < 2 ** self.level:
                    left -= self.A[curr + 1]
            else:
                curr = curr * 2 + 1
        return left


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)