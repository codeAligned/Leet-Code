class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) / 2
        
        # Memorization Solution
        
        d = [{} for i in nums]
        
        def check(curr_pos, curr_target):
            if curr_target == 0:
                return True
            if curr_target < 0:
                return False
            if curr_pos == len(nums):
                return curr_target == 0
                
            if curr_target in d[curr_pos]:
                return d[curr_pos][curr_target]
            
            # # include the number in curr_pos
            # ret_1 = check(curr_pos + 1, curr_target - nums[curr_pos])
            
            # # do not include the number in curr_pos
            # ret_2 = check(curr_pos + 1, curr_target)
            # d[curr_pos][curr_target] = ret_1 or ret_2
            # return ret_1 or ret_2
            
            # These two steps can be combined in the following loop
            for i in range(curr_pos + 1, len(nums)):
                if check(i, curr_target - nums[i]):
                    d[curr_pos][curr_target] = True
                    return True
                    
            d[curr_pos][curr_target] = False
            return False
            
        return check(0, target)