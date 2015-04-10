class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    # O(n ^ 2) Solution
    def threeSum(self, num):
        ret = []
        num = sorted(num)
        for k in range(len(num) - 2):
            # get rid of the duplicates - num[k] != num[k - 1]
            if k == 0 or k > 0 and num[k] != num[k - 1]:
                i, j, t = k + 1, len(num) - 1, -num[k]
                while i < j:
                    n = num[i] + num[j]
                    if t > n:
                        i += 1
                    elif t < n:
                        j -= 1
                    else:
                        ret.append([num[k], num[i], num[j]])
                        # get rid of the duplicates - two while loops
                        while i < j and num[i] == num[i + 1]:
                            i += 1
                        while i < j and num[j] == num[j - 1]:
                            j -= 1
                        i += 1
                        j -= 1
        return ret

s = Solution()
print s.threeSum([0,0,0])