class Solution:
    # @param s, a string
    # @return a boolean

    # DFA-based Solution
    def isNumber(self, s):
        state = 0
        s = s.strip()
        for c in s:
            if c in ['+', '-']:
                if state == 0: state = 1
                elif state == 3: state = 4
                else: return False
            elif c == '.':
                if state in [0, 1]: state = 6
                elif state == 2: state = 7
                else: return False
            elif c == 'e':
                if state in [2, 7]: state = 3
                else: return False
            elif c.isdigit():
                if state in [0, 1, 2]: state = 2
                elif state in [6, 7]: state = 7
                elif state in [3, 4, 5]: state = 5
                else: return False
            else:
                return False
        if state in [2, 5, 7]:
            return True
        else:
            return False