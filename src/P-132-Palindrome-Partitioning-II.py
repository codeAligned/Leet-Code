'''
P-132 - Palindrome Partitioning II

Given a strings, partitionssuch that every substring of the partition
is a palindrome. Return the minimum cuts needed for a palindrome
partitioning ofs. For example, givens="aab",Return1since the
palindrome partitioning["aa","b"]could be produced using 1 cut.

Tags: Dynamic Programming
'''

class Solution:
    # @param s, a string
    # @return an integer

    # DP-based Solution
    def minCut(self, s):
        n = len(s)
        # cut[k] is the number of cuts for the first k characters
        cut = range(-1, n)
        for i in range(n):
            # Odd length palindrome
            for j in range(min(n - i, i + 1)):
                if s[i - j] != s[i + j]:
                    break
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j])
            # Even length palindrome
            for j in range(1, min(i + 2, n - i)):
                if s[i - j + 1] != s[i + j]:
                    break
                cut[i + j + 1] = min(cut[i + j + 1], 1 + cut[i - j + 1])
        return cut[n]