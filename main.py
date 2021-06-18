from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        # Method 1
            
#         tar = len(graph) - 1
#         res = []
#         traversalList = [0]
#         visited = set()
#         currNode = traversalList[0]
        
#         self.allPathsHelper(graph, visited, currNode, traversalList, res, tar)
#         return sorted(res)
            
#     def allPathsHelper(self, graph, visited, currNode, traversalList, res, tar):
        
#         if currNode == tar:
#             res.append(traversalList)
#             return
        
#         neighbors = graph[currNode]
        
#         for i in neighbors:
#             if i not in visited:
#                 self.allPathsHelper(graph, visited, i, traversalList + [i], res, tar)
                
        # Method 2 (DFS)
        
        '''
        
        P:
        
        1. Translate the problem into graph terminology
            * vertices - each index in the list
            * edges - each element in the sublist is an outgoing edge 
              of the node at index i
            * weight - n/a
            
        2. Build your graph
            * You can build your own graph using adjacency list
            * Or you can just traverse the nested list
            
        3. Traverse the graph
            * Traversal doesn't matter since we're looking for all possible paths
            * Use a DFS
            * Use an auxillary array and also put it in the stack to keep track of the               path to get the current node
        '''
        
#         destinationNode = len(graph) - 1
#         graph = self.buildGraph(graph)
#         stack = deque()
#         stack.append((0, [0]))
#         res = []
#         while len(stack) > 0:
#             curr = stack.pop()
#             currNode, currPath = curr[0], curr[1]
#             if currNode == destinationNode:
#                 res.append(currPath)
#             else:
#                 for neighbor in graph[currNode]:
#                     newPath = currPath.copy()
#                     newPath.append(neighbor)
#                     stack.append((neighbor, newPath))
                    
#         return res
        
#     def buildGraph(self, edges):
#         graph = {}
            
#         for (node, neighbors) in enumerate(edges):
#             graph[node] = set() 
#             for neighbor in neighbors:
#                 graph[node].add(neighbor)
#         return graph


        # Method 3 (BFS)
    
        destinationNode = len(graph) - 1
        graph = self.buildGraph(graph)
        queue = deque()
        queue.append((0, [0]))
        res = []
        while len(queue) > 0:
            curr = queue.popleft()
            currNode, currPath = curr[0], curr[1]
            if currNode == destinationNode:
                res.append(currPath)
            else:
                for neighbor in graph[currNode]:
                    newPath = currPath.copy()
                    newPath.append(neighbor)
                    queue.append((neighbor, newPath))
                    
        return res
        
    def buildGraph(self, edges):
        graph = {}
            
        for (node, neighbors) in enumerate(edges):
            graph[node] = set() 
            for neighbor in neighbors:
                graph[node].add(neighbor)
        return graph