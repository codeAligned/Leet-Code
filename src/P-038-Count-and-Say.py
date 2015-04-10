class Solution:
    # @return a string
    def countAndSay(self, n):
        ret = '1'
        for k in range(1, n):
            tmp = ''
            curr = ret[0]
            count = 1
            for i in range(1, len(ret)):
                if ret[i] == curr:
                    count += 1
                else:
                    tmp += str(count) + str(curr)
                    curr = ret[i]
                    count = 1
            # Count the last one
            tmp += str(count) + str(curr)
            ret = tmp
        return ret