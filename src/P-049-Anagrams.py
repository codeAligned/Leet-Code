class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        m = {}
        for string in strs:
            h = ''.join(sorted(string))
            if h in m:
                m[h].append(string)
            else:
                m[h] = [string, ]
        return reduce(lambda x, y: x + y, filter(lambda x: len(x) > 1, m.values()), [])

s = Solution()
l = ['abc', 'cba', 'abcc', 'abbc', 'acbb']
print s.anagrams(l)