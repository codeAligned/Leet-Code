class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {word: index for index, word in enumerate(words)}
        ret = []
        
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix = w[:j]
                postfix = w[j:]
                
                if prefix[::-1] in d and d[prefix[::-1]] != i and postfix == postfix[::-1]:
                    ret.append([i, d[prefix[::-1]]])
                if j > 0 and postfix[::-1] in d and d[postfix[::-1]] != i and prefix == prefix[::-1]:
                    ret.append([d[postfix[::-1]], i])
        return ret