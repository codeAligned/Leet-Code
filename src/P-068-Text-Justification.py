'''
P-068 - Text Justification

Given an array of words and a lengthL, format the text such that each
line has exactlyLcharacters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many
words as you can in each line. Pad extra spaces' 'when necessary so
that each line has exactlyLcharacters. Extra spaces between words
should be distributed as evenly as possible. If the number of spaces
on a line do not divide evenly between words, the empty slots on the
left will be assigned more spaces than the slots on the right. For the
last line of text, it should be left justified and no extra space is
inserted between words. For example,words:["This", "is", "an",
"example", "of", "text", "justification."]L:16. Return the formatted
lines as:[     "This    is    an",     "example  of text",
"justification.  "  ] Note:Each word is guaranteed not to exceedLin
length. click to show corner cases. A line other than the last line
might contain only one word. What should you do in this case?In this
case, that line should be left-justified.

Tags: String
'''

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