# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def __init__(self):
        self.delim = ','
        self.end_sign = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        ret = []

        def aux(node):
            if not node:
                ret.append(self.end_sign + self.delim)
            else:
                ret.append(str(node.val) + self.delim)
                aux(node.left)
                aux(node.right)
        
        aux(root)
        
        return ''.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        self.curr = 0
        def aux():
            prev = self.curr
            while self.curr < len(data) and data[self.curr] != self.delim:
                self.curr += 1
            s = data[prev:self.curr]
            self.curr += 1
            if s == self.end_sign:
                return None
            else:
                node = TreeNode(int(s))
                node.left = aux()
                node.right = aux()
                return node
            
        return aux()

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))