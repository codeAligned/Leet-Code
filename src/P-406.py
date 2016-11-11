class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        
        # Sort the people first decreasing order w.r.t h and then increasing order w.r.t k
        people.sort(cmp=lambda x, y: x[1] - y[1] if x[0] == y[0] else y[0] - x[0])

        # Insert each [h, k] into k th position
        for h, k in people:
            ret.insert(k, [h, k])
            
        return ret
            