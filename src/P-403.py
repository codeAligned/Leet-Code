class Solution(object):
    def canCross(self, stones):
        steps={key:[] for key in stones}
        steps[0].append(0)
        for i in xrange(len(stones)):
            for j in steps[stones[i]]:
                for jump in (j-1,j,j+1):
                    nxt = stones[i]+jump
                    if nxt==stones[-1]:
                        return True
                    if nxt in steps and (not steps[nxt] or steps[nxt][-1]>jump):
                        steps[nxt].append(jump)
        return False