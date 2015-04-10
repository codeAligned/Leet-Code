class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    # O(n^2*log(n))
    def fourSum(self, num, target):
        num.sort()
        m = {}
        ret = set()
        for i in range(len(num)):
            for j in range(i + 1, len(num)):
                s = num[i] + num[j]
                if s not in m:
                    m[s] = []
                m[s].append((i, j))
        vals = sorted(m.keys())
        i, j = 0, len(vals) - 1
        while i <= j:
            s = vals[i] + vals[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                for a, b in m[vals[i]]:
                    for c, d in m[vals[j]]:
                        if len(set([a, b, c, d])) == 4:
                            ret.add(tuple(sorted([num[a], num[b], num[c], num[d]])))
                i += 1
                j -= 1
        return [list(item) for item in ret]

s = Solution()
print s.fourSum([1,0,-1,0,-2,2], 0)
print s.fourSum([-3,-1,0,2,4,5], 0)