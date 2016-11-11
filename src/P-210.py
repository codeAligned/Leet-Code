class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        grey = -1
        black = -2
        
        g = [set() for _ in range(numCourses)]
        
        for c, p in prerequisites:
            g[p].add(c)
            
        ret = []
        
        self.fail = False
    
        def dfs(c):
            if grey in g[c]:
                self.fail = True
                return 
            elif black in g[c]:
                return
            else:
                g[c].add(grey)
                for n in g[c] - {grey}:
                    dfs(n)
                g[c].remove(grey)
                g[c].add(black)
                ret.insert(0, c)
        
        def next_white(prev):
            for i in range(prev, numCourses):
                if black not in g[i] and grey not in g[i]:
                    return i
            return None
        
        next = 0
        
        while next is not None:
            dfs(next)
            if self.fail:
                return []
            next = next_white(next)
        
        return ret