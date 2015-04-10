class Solution:
    # @param s, a string
    # @return a list of strings
    def aux(self, comb = [], start = 0, level = 0):
        i = 1
        if level == 4:
            if start == len(self.s):
                self.ret.append(''.join(str(item) + '.' for item in comb)[:-1])
            return
        while start + i <= len(self.s):
            num = int(self.s[start : start + i])
            if num < 256 and len(str(num)) == i:
                comb.append(num)
                self.aux(comb, start + i, level + 1)
                comb.pop()
                i += 1
            else:
                break
        return self.ret

    def restoreIpAddresses(self, s):
        self.ret, self.s = [], s
        return self.aux()

s = Solution()
ip = '25525511135'
ip = '0000'
ip = '010010'
for item in s.restoreIpAddresses(ip):
    print item