'''
P-089 - Gray Code

The gray code is a binary numeral system where two successive values
differ in only one bit. Given a non-negative integernrepresenting the
total number of bits in the code, print the sequence of gray code. A
gray code sequence must begin with 0. For example, givenn= 2,
return[0,1,3,2]. Its gray code sequence is: Note:For a givenn, a gray
code sequence is not uniquely defined. For example,[0,2,3,1]is also a
valid gray code sequence according to the above definition. For now,
the judge is able to judge based on one instance of gray code
sequence. Sorry about that.

Tags: Backtracking
'''

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