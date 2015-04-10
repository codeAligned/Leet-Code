class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        m = [0] * len(num)
        if len(num) == 0:
            return 0
        elif len(num) == 1:
            return num[0]
        elif len(num) == 2:
            return max(num[1], num[0])
        else:
            m[-1] = num[-1]
            m[-2] = max(num[-1], num[-2])
            for i in reversed(range(len(num) - 2)):
                m[i] = max(num[i] + m[i + 2], m[i + 1])
            return m[0]