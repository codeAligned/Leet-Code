class Solution:
    # @return an integer
    # Spoiler:
    # - Discard the leading zeros or whitespaces
    # - Interpret as many digits as possible
    # - Discard any trailing characters
    # - Return 0 if input not valid
    # - Deal with overflow
    def atoi(self, str):
        limit = 2 ** 31
        n = 0
        negative = False
        starting = True
        for c in str:
            if starting:
                if c == '+':
                    starting = False
                    continue
                if c == '-':
                    starting = False
                    negative = True
                    continue
                if c == '0' or c == ' ' :
                    continue
            if ord(c) <= ord('9') and ord(c) >= ord('0'):
                n = n * 10 + int(c)
                starting = False
            else:
                break
        n = -n if negative else n
        if n >= limit:
            n = limit - 1
        if n < -limit:
            n = -limit
        return n

s = Solution()

print s.atoi('123')
print s.atoi('1230')
print s.atoi('-123')
print s.atoi('0123')
print s.atoi('+123')
print s.atoi('-0123')
print s.atoi(' 123')
print s.atoi('- 0123')
