class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        ####### DP Solution #######
        ### d[m][k] = for i = k + 1 to n - m + 1, min(max(nums[k:i], d[m - 1][i]))
        ### d[m][k] means the min max with m spilts in nums[k:]
        
        # n = len(nums)
        
        # d = [[0] * n for i in range(m + 1)]
        # S = [0]
        # for i in xrange(n):
        #   S.append(S[-1] + nums[i])
        
        # for i in xrange(n):
        #   d[0][i] = S[n] - S[i]

        # for i in xrange(1, m):
        #   for k in xrange(n - i):
        #       my_min = 2147483649
        #       for j in xrange(k + 1, n - i + 1):
        #           t = max(S[j] - S[k], d[i - 1][j])
        #           if t <= my_min:
        #               my_min = t
        #           else:
        #               break
        #       d[i][k] = my_min
        
        # return d[-1][0]

        ####### Binary Search Solution #######

        def valid(mid):
            split = 0
            temp_sum = 0
            for curr in nums:
                if temp_sum + curr <= mid:
                    temp_sum += curr
                else:
                    temp_sum = curr
                    split += 1
                if curr > mid or split >= m:
                    return False
            return True

        high = sum(nums)
        low = max(high / m, max(nums))

        while low <= high:
            print low, high
            mid = (high + low) / 2
            if valid(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low