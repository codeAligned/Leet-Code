from copy import copy

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        n = len(L[0])
        m = {word: L.count(word) for word in L}
        ret = []
        for k in range(n):
            curr_start = k
            curr_total = 0
            counter = {}
            for i in range(k, len(S), n):
                word = S[i : i + n]
                if word in m:
                    if word not in counter:
                        counter[word] = 0
                    counter[word] += 1
                    if counter[word] > m[word]:
                        while counter[word] > m[word]:
                            tw = S[curr_start : curr_start + n]
                            counter[tw] -= 1
                            if counter[tw] < m[word]:
                                curr_total -= 1
                            curr_start += n
                    else:
                        curr_total += 1
                    if curr_total == len(L):
                        ret.append(curr_start)
                        counter[S[curr_start : curr_start + n]] -= 1
                        curr_total -= 1
                        curr_start += n
                else:
                    counter = {}
                    curr_total = 0
                    curr_start = i + n
        return ret

    # Without curr_total
    # Use copy and decrement the counter everytime
    # simpler code but slower
    def findSubstring(self, S, L):
        n = len(L[0])
        m = {word: L.count(word) for word in L}
        ret = []
        for k in range(n):
            curr_start = k
            counter = copy(m)
            for i in range(k, len(S), n):
                word = S[i : i + n]
                if word in m:
                    counter[word] -= 1
                    while counter[word] < 0:
                        counter[S[curr_start : curr_start + n]] += 1
                        curr_start += n
                    if sum(counter.values()) == 0:
                        ret.append(curr_start)
                        counter[S[curr_start : curr_start + n]] += 1
                        curr_start += n
                else:
                    counter = copy(m)
                    curr_start = i + n
        return ret

s = Solution()

S = "barfoothefoobarman"
L = ['foo', 'bar']
S = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
L = ["fooo","barr","wing","ding","wing"]

print s.findSubstring(S, L)