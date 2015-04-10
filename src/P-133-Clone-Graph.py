   def cloneGraph(self, node):
        if not node:
            return None
        self.newNodeDict={}
        return self.createNode(node)

    def createNode(self, oldNode):
        newNode = UndirectedGraphNode(oldNode.label)
        self.newNodeDict[newNode.label] = newNode

        for i in oldNode.neighbors:
            if i.label not in self.newNodeDict:
                self.createNode(i) #recursively create nodes
            newNode.neighbors.append(self.newNodeDict[i.label])
        return newNode  