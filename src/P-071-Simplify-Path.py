class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        ret = ''
        stack = []
        for item in path.strip('/').split('/'):
            if item == '.':     # stay at current dir
                continue
            elif item == '..':  # goto upper level
                if len(stack) != 0: # if there is any level other than root
                    stack.pop()
                else:
                    continue    # we got the root, continue
            elif item == '':    # deal with multiple slashes
                continue
            else:
                stack.append(item)
        for item in stack:
            ret += '/' + str(item)
        if len(ret) == 0:
            ret += '/'
        return ret

s = Solution()

print s.simplifyPath('/home//b//')
print s.simplifyPath('/a/./b/../../c/')
print s.simplifyPath('/.././')