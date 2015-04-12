'''
P-187 - Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G,
and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes
useful to identify repeated sequences within the DNA. Write a function
to find all the 10-letter-long sequences (substrings) that occur more
than once in a DNA molecule. For example,

Tags: Hash Table, Bit Manipulation
'''

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