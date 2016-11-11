_end = '_'

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.t = make_trie(*words)

        if board == None:
            return None

        self.b = board
        self.result = set([])

        self.height = len(board)
        self.width = len(board[0])

        self.flags = [[False for i in range(self.width)] for j in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                self.find(x, y, '', self.t)

        return list(self.result)

    def find(self, x, y, my_str, prev):
        self.flags[x][y] = True
        if self.b[x][y] in prev:
            prev = prev[self.b[x][y]]
            my_str += self.b[x][y]
            if _end in prev:
                self.result.add(my_str)
            for nx, ny in filter(lambda (x, y): x >= 0 and y >= 0 and x < self.height and y < self.width, [(x-1, y), (x + 1, y), (x, y-1), (x, y+1)]):
                if not self.flags[nx][ny]:
                    self.find(nx, ny, my_str, prev)
        self.flags[x][y] = False