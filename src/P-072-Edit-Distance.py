'''
P-072 - Edit Distance

Given two wordsword1andword2, find the minimum number of steps
required to convertword1toword2. (each operation is counted as 1
step.) You have the following 3 operations permitted on a word: a)
Insert a characterb) Delete a characterc) Replace a character

Tags: Dynamic Programming, String
'''

class Solution:
    # @return an integer

    # DP-based Solution
    # start from small strings of both word1 and word2
    # m[i][j] means how much step to make word1[:i + 1] and word2[: j + 1] same
    def minDistance(self, word1, word2):
        m = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            m[i][0] = i
        for j in range(1, len(word2) + 1):
            m[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                m[i][j] = min(
                                m[i - 1][j] + 1,
                                m[i][j - 1] + 1,
                                m[i - 1][j - 1] if word2[j - 1] == word1[i - 1] else m[i - 1][j - 1] + 1
                    )
        return m[len(word1)][len(word2)]

s = Solution()
print s.minDistance('ABCDE', 'ADE')
