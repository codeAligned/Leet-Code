class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer

    # Brute-Force
    def strStr(self, haystack, needle):
        n, m, i = len(haystack), len(needle), 0
        while i <= n - m:
            if haystack[i : i + m] == needle:
                return i
            i += 1
        return -1
        
    '''
    # Rabin-Karp Algorithm
    def strStr(self, string, target):
        n, m = len(string), len(target)
        h, q = 10 ** (m - 1) % (2 ** 31), 2 ** 31
        target_hash = string_hash = 0 
        if n < m:
            return -1
        for i in range(m):
            target_hash = (target_hash * 10 + ord(target[i])) % q
            string_hash = (string_hash * 10 + ord(string[i])) % q
        for k in range(n - m + 1):
            if target_hash == string_hash and target == string[k : k + m]:
                return k
            if k < n - m:
                string_hash = (10 * (string_hash - ord(string[k]) * h) + ord(string[k + m])) % q
        return -1
    '''

    # KMP Algorithm
    def kmp_prefix(self, pattern):
        p = [-1] * (len(pattern) + 1)
        for i in range(len(pattern)):
            p[i + 1] = p[i] + 1
            while p[i + 1] > 0 and pattern[i] != pattern[p[i + 1] - 1]:
                p[i + 1] = p[p[i + 1] - 1] + 1
        return p

    def kmp(self, s, p):
        j = 0
        prefix = self.kmp_prefix(p)
        for i in range(len(s)):
            while True:
                if s[i] == p[j]:
                    j += 1
                    if j == len(p):
                        #print 'match at %d' % i
                        return i
                        j = prefix[j]
                    break
                elif j == 0:
                    break
                else:
                    j = prefix[j]
        return -1

s = Solution()
print s.strStr("mississippi", "issipi")
print s.strStr("", "")   
        