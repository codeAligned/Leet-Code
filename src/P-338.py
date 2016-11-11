class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0, 1]
        
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        else:
            while True:
                size = len(ret)
                for i in xrange(size):
                    ret.append(1 + ret[i])
                    if len(ret) == num + 1:
                        return ret