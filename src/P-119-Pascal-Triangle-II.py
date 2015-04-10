class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        row = [1]
        for k in range(1, rowIndex + 1):
            tmp = [1]
            for i in range(1, k):
                tmp.append(row[i - 1] + row[i])
            tmp.append(1)
            row = tmp
        return row

s = Solution()

print s.getRow(4)