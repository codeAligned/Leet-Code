from collections import defaultdict

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def next_word(self, word, dict):
        alpha = set('abcdefghijklmnopqrstuvwxyz')
        for i, c in enumerate(word):
            for l in alpha - {c}:
                w = word[:i] + l + word[i + 1:]
                if w in dict:
                    yield w

    def gen_path(self, start, end, tree):
        # start from the end
        path_list = [[end, ], ]
        # while not reaching the start
        while path_list[0][0] != start:
            # add the parent to the first node in each path until we reach start
            path_list = [[prev] + path for path in path_list for prev in tree[path[0]]]
        return path_list

    def findLadders(self, start, end, dict):
        dict.add(end)
        visit_tree = {}
        curr_queue = {start}
        while curr_queue:
            curr_visit = defaultdict(set)
            next_queue = set()
            for word in curr_queue:
                for next in self.next_word(word, dict):
                    if next not in visit_tree:
                        # use a set for queue because next may be duplicates
                        next_queue.add(next)
                        # and we have to keep track of those duplicates
                        # in order to generate all the pathes
                        curr_visit[next].add(word)
            visit_tree.update(curr_visit)
            curr_queue = next_queue
            if end in visit_tree:
                return self.gen_path(start, end, visit_tree)
        return []

s = Solution()
start = "hit"
end = "cog"
dict = set(["hot","dot","dog","lot","log"])

for item in s.findLadders(start, end, dict):
    print item