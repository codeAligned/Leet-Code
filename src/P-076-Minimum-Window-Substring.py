class Solution:
    # @return a string
    def minWindow(self, S, T):
        curr_min = curr_pos = len(S)
        start = 0
        t_map = {c: T.count(c) for c in T}
        for index, char in enumerate(S):
            if char in t_map:
                t_map[char] -= 1
            # if all characters are in the current substring
            if reduce(lambda x, y: x and t_map[y] <= 0, t_map, True):
                while S[start] not in t_map or t_map[S[start]] < 0:
                    if S[start] in t_map:
                        t_map[S[start]] += 1
                    start += 1
                if curr_min >= index - start + 1:
                    curr_min, curr_pos = index - start + 1, start
        return S[curr_pos: curr_pos + curr_min]


s = Solution()
S = "ADOBECODEBANC"; T = "ABC"
S = "A"; T = "A"
S = 'bdab'; T = 'ab'
S = "cabwefgewcwaefgcf"; T = "cae"
S = "caae"; T = "cae"
S = "bba"; T = "ab"
S = "a"; T = "aa"
print s.minWindow(S, T)