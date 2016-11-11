class Solution(object):

    def process_str(self, s):

        idx = 0     # Current index
        num = 0     # k
        st = 0      # Start point of current encoding unit
        sst = 0     # Start point of substr
        cnt = 0     # Use for finding the corresponding ]

        ret_s = ''

        found = False

        while idx < len(s):
            
            # Find the first [, if not found, return the whole string
            while idx < len(s):
                if s[idx] == '[':
                    found = True
                    break
                idx += 1
            if not found:
                return s

            # Separate the extra string and the num
            found = False
            for i in range(st, idx):
                if s[i].isdigit():
                    found = True
                    break
            if found:
                num = int(s[i:idx])
                extra_s = s[st:i]
            else:
                num = 0
                extra_s = s[st:idx]

            # Find the corresponding ]
            idx += 1
            sst = idx
            while idx < len(s):
                if s[idx] == '[':
                    cnt += 1
                elif s[idx] == ']':
                    if cnt == 0:
                        break
                    else:
                        cnt -= 1
                idx += 1

            # Recursively on the sub string
            ret_s += extra_s + self.process_str(s[sst: idx]) * num

            # Continue scanning the rest of the string 
            idx += 1
            st = idx

        return ret_s

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.process_str(s)