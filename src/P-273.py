class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        w1 = ['Zero ', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', ]
        w2 = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
        w3 = ['Ten ', "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]
        w4 = ['', 'Thousand ', 'Million ', 'Billion ', ]
        
        ret = []
        
        groups = []
        
        if num == 0:
            return 'Zero'
        
        num_str = list(reversed(str(num)))
        
        for i in xrange(0, len(num_str), 3):
            groups.append([int(c) for c in num_str[i : i+3]])
        
        for i, g in enumerate(groups):
            prev_pos = len(ret)
            if len(g) == 1:
                if g[0] != 0:
                    ret.append(w1[g[0]])
            if len(g) == 2:
                if g[1] == 1:
                    ret.append(w3[g[0]])
                else:
                    if g[0] != 0:
                        ret.append(w1[g[0]])
                    ret.append(w2[g[1]])
            if len(g) == 3:
                if g[1] == 1:
                    ret.append(w3[g[0]])
                elif g[1] > 1:
                    if g[0] != 0:
                        ret.append(w1[g[0]])
                    ret.append(w2[g[1]])
                else:
                    if g[0] != 0:
                        ret.append(w1[g[0]])
                if g[2] != 0:
                    ret.append(w1[g[2]] + "Hundred ")
                   
            if prev_pos != len(ret):
                ret.insert(prev_pos, w4[i])
            
        return ''.join(reversed(ret)).strip()