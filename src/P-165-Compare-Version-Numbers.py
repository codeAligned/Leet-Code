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