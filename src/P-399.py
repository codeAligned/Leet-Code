class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        import itertools

        d = {}
        
        for (x, y), v in zip(equations, values):
            if x not in d:
                d[x] = {}
            if y not in d:
                d[y] = {}
            d[x][x] = 1.0
            d[y][y] = 1.0
            d[x][y] = v
            d[y][x] = 1/v
        for x, y, z in itertools.permutations(d, 3):
            if y in d[x] and z in d[y]:
                d[x][z] = d[x][y] * d[y][z]

        ret = []
        for x, y in queries:
            if x in d and y in d[x]:
                ret.append(d[x][y])
            elif y in d and x in d[y]:
                ret.append(1/d[y][x])
            else:
                ret.append(-1.0)
            
        return ret      
                    
        
            