class Solution:
    # @return a string
    def convert(self, s, nRows):
        rows = [[] for n in range(nRows)]
        i = 0
        while i < len(s):
            # Down
            for row in rows:
                if i < len(s):
                    row.append(s[i])
                i += 1
            # Up
            for row in rows[-2:0:-1]:
                if i < len(s):
                    row.append(s[i])
                i += 1
        return ''.join([''.join(row) for row in rows])

s = Solution()

print "PAHNAPLSIIGYIR"
print s.convert("PAYPALISHIRING", 3)