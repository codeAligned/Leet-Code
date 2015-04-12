'''
P-031 - Next Permutation

Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers. If such
arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order). The replacement must
be in-place, do not allocate extra memory. Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are
in the right-hand
column.1,2,3&#8594;1,3,23,2,1&#8594;1,2,31,1,5&#8594;1,5,1

Tags: Array
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num,):
        flag = False
        if len(num) == 1:
            return num
        for i in reversed(xrange(1, len(num))):
            # find the first place from the end that descending
            if num[i] > num[i - 1]:
                flag = True

                # find the lowest value from i to end that is greater than num[i-1]
                t = i
                for j in range(i, len(num)):
                    if num[i - 1] < num[j] and num[t] > num[j]:
                        t = j
                # swap
                num[i - 1], num[t] = num[t], num[i - 1]

                # sort
                for m in range(i, len(num)):
                    for n in range(m + 1, len(num)):
                        if num[m] > num[n]:
                            num[m], num[n] = num[n], num[m]
                break
        if not flag:
            i = 0
            while i < len(num) - i - 1:
                num[i], num[len(num) - i - 1] = num[len(num) - i - 1], num[i]
                i += 1
        return num

s = Solution()

l = [1,3,2,4,5]
c = [1,3,2,4,5]

l = [1,3,4,5]
c = [1,3,4,5]

t = s.nextPermutation(l)
while t != c:
    print t
    t = s.nextPermutation(t)