class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        s = []
        
        preorder = preorder.split(',')
        
        for c in preorder:
            while(len(s) > 2 and s[-1] == '#' and s[-2] == '#' and s[-3] != '#'):
                s.pop()
                s.pop()
                s.pop()
                s.append('#')
            s.append(c)
        
        while(len(s) > 2 and s[-1] == '#' and s[-2] == '#' and s[-3] != '#'):
            s.pop()
            s.pop()
            s.pop()
            s.append('#')
        
        if len(s) == 1 and s[0] == '#':
            return True
        else:
            return False