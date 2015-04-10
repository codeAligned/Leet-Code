class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        k = 0
        m = len(min(strs, key=lambda x: len(x)))
        while k < m:
            c = strs[0][k]
            for s in strs:
                if s[k] != c:
                    return strs[0][:k]
            k += 1
        return strs[0][:k]

    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) > 1:
                return strs[0][:i]
        return min(strs)