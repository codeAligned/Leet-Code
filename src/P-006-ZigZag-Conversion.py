'''
P-006 - ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR" Write the code that will
take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Tags: String
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        rows = [[] for n in range(nRows)]
        i = 0
        while i < len(s):
            # Down
            for row in rows:
                if i < len(s):
                    row.append(s[i])
                i += 1
            # Up
            for row in rows[-2:0:-1]:
                if i < len(s):
                    row.append(s[i])
                i += 1
        return ''.join([''.join(row) for row in rows])

# Testing
from utils import *

cases = [
	Test_case(("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
]

run_cases(Solution().convert, cases)
