class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        m = {}
        ret = []
        for i in range(len(s) - 9):
            word = s[i : i + 10]
            if word in m:
                if m[word] == 1:
                    ret.append(word)
                m[word] += 1
            else:
                m[word] = 1
        return ret

l = "AAAAAAAAAAA"
s = Solution()

print s.findRepeatedDnaSequences(l)