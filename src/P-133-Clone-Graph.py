'''
P-133 - Clone Graph

Clone an undirected graph. Each node in the graph contains alabeland a
list of itsneighbors. Nodes are labeled uniquely. As an example,
consider the serialized graph{0,1,2#1,2#2,2}. The graph has a total of
three nodes, and therefore contains three parts as separated by#.First
node is labeled as0. Connect node0to both nodes1and2.Second node is
labeled as1. Connect node1to node2.Third node is labeled as2. Connect
node2to node2(itself), thus forming a self-cycle. Visually, the graph
looks like the following:1        / \       /   \      0 --- 2
/ \           \_/

Tags: Depth-first Search, Breadth-first Search, Graph
'''

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