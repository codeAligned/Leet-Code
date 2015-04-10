class Solution:
    # @return a list of integers

    # Gray code with n bits
    # The last i bit has to be flipped every 2^i numbers 
    # unless higher bits has been flipped
    def grayCode(self, n):
        ret, num = [0, ], 0
        for i in xrange(1, 2 ** n):
            for j in reversed(xrange(n)):
                if i % (2 ** j) == 0:
                    # flip jth bit of num
                    num ^= (1 << j)
                    break
            ret.append(num)
        return ret

s = Solution()
n = 4
for item in s.grayCode(n):
    print ('%' + str(len(str(2 ** n))) + 'd' ) % item, (n - len(bin(item)[2:])) * '0' + bin(item)[2:]