'''
P-165 - Compare Version Numbers

Compare two version
numbersversion1andversion2.Ifversion1&gt;version2return 1,
ifversion1&lt;version2return -1, otherwise return 0. You may assume
that the version strings are non-empty and contain only digits and
the.character.The.character does not represent a decimal point and is
used to separate number sequences.For instance,2.5is not "two and a
half" or "half way to version three", it is the fifth second-level
revision of the second first-level revision. Here is an example of
version numbers ordering: Credits:Special thanks to@tsfor adding this
problem and creating all test cases.

Tags: String
'''

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1, v2 = version1.split('.'), version2.split('.')

        for i in range(max(len(v1), len(v2))):
        	n1 = int(v1[i]) if i < len(v1) else 0
        	n2 = int(v2[i]) if i < len(v2) else 0
        	if n1 > n2:
        		return 1
        	elif n1 < n2:
        		return -1
        return 0

s = Solution()

print s.compareVersion('1.0.0','1')