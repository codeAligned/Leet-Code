class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        curr = 0
        ret = []

        while curr < len(words):
            char = 0
            space = -1
            row = []
            while curr < len(words) and char + space + len(words[curr]) + 1 <= L:
                    if row:
                        row.append(' ')
                    row.append(words[curr])
                    char += len(words[curr])
                    space += 1
                    curr += 1
            pad = L - char - space
            if space and curr < len(words):
                pad_per_space, pad_extra = divmod(pad, space)
                for j in range(space):
                    row[2 * j + 1] += ' ' * (pad_per_space + 1 if j < pad_extra else pad_per_space)
            else:
                row.append(' ' * pad)
            ret.append(''.join(row))
        return ret

s = Solution()
w = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
w = ["What","must","be","shall","be."]
L = 12
for item in s.fullJustify(w, L):
    print len(item), item