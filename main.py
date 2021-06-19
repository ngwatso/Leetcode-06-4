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
    
#         destinationNode = len(graph) - 1
#         graph = self.buildGraph(graph)
#         queue = deque()
#         queue.append((0, [0]))
#         res = []
#         while len(queue) > 0:
#             curr = queue.popleft()
#             currNode, currPath = curr[0], curr[1]
#             if currNode == destinationNode:
#                 res.append(currPath)
#             else:
#                 for neighbor in graph[currNode]:
#                     newPath = currPath.copy()
#                     newPath.append(neighbor)
#                     queue.append((neighbor, newPath))
                    
#         return res
        
#     def buildGraph(self, edges):
#         graph = {}
            
#         for (node, neighbors) in enumerate(edges):
#             graph[node] = set() 
#             for neighbor in neighbors:
#                 graph[node].add(neighbor)
#         return graph


        # Method 4 (recursion)
    
        res = []
        self.allPathsHelper(graph, 0, len(graph) - 1, [0], res)
        return res
    
    def allPathsHelper(self, graph, currNode, destinationNode, currPath, res):
        if currNode == destinationNode:
            res.append(currPath)
        else:
            for neighbor in graph[currNode]:
                newPath = currPath.copy()
                newPath.append(neighbor)
                self.allPathsHelper(graph, neighbor, destinationNode, newPath, res)


# ===============


from collections import deque

class Solution:
    
    '''

    [[1,1,1],
     [1,1,0],
     [1,0,1]]
     sr = 1
     sc = 1
     newColor = 2

    [[2,2,2],
     [2,2,0],
     [2,0,1]]
     sr = 2
     sc = 2
     newColor = 3

     [[2,2,2],
      [2,2,0],
      [2,0,3]]

      P:

      1. Translate:
        * vertices - pixels
        * edges - direct neighbors (up, down, left, right)
        * weights - n/a

      2. Build your graph:
        * No need to build a graph, just traverse the image given

      3. Traverse the graph:
        * It doesn't matter as long as you traverse all neighboring nodes with same value       as starting node

    '''

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # Method 1 - DFS
        
#         colorToChange = image[sr][sc]
#         stack = deque()
#         stack.append((sr, sc))
#         visited = set()
#         numRows, numCols = len(image), len(image[0])
        
#         while len(stack) > 0:
#             currPixel = stack.pop()
#             if currPixel in visited:
#                 continue
#             currRow, currCol = currPixel[0], currPixel[1]
#             image[currRow][currCol] = newColor
#             visited.add(currPixel)
            
#             topRow = currRow - 1
#             if topRow >= 0 and image[topRow][currCol] == colorToChange:
#                 stack.append((topRow, currCol))
                
#             bottomRow = currRow + 1
#             if bottomRow < numRows and image[bottomRow][currCol] == colorToChange:
#                 stack.append((bottomRow, currCol))
                
#             leftCol = currCol - 1
#             if leftCol >= 0 and image[currRow][leftCol] == colorToChange:
#                 stack.append((currRow, leftCol))
                
#             rightCol = currCol + 1
#             if rightCol < numCols and image[currRow][rightCol] == colorToChange:
#                 stack.append((currRow, rightCol))
                
#         return image


        # Method 2 - BFS
    
        colorToChange = image[sr][sc]
        queue = deque()
        queue.append((sr, sc))
        visited = set()
        numRows, numCols = len(image), len(image[0])
        
        while len(queue) > 0:
            currPixel = queue.popleft()
            if currPixel in visited:
                continue
            currRow, currCol = currPixel[0], currPixel[1]
            image[currRow][currCol] = newColor
            visited.add(currPixel)
            
            topRow = currRow - 1
            if topRow >= 0 and image[topRow][currCol] == colorToChange:
                queue.append((topRow, currCol))
                
            bottomRow = currRow + 1
            if bottomRow < numRows and image[bottomRow][currCol] == colorToChange:
                queue.append((bottomRow, currCol))
                
            leftCol = currCol - 1
            if leftCol >= 0 and image[currRow][leftCol] == colorToChange:
                queue.append((currRow, leftCol))
                
            rightCol = currCol + 1
            if rightCol < numCols and image[currRow][rightCol] == colorToChange:
                queue.append((currRow, rightCol))
                
        return image


        # Method 3 - recursive
    
        visited = set()
        self.floodHelper(image, sr, sc, image[sr][sc], newColor, visited)
        return image
    
    def floodHelper(self, image, currRow, currCol, colorToChange, newColor, visited):
        numRows, numCols = len(image), len(image[0])
        if currRow < 0 or currRow >= numRows or currCol < 0 or currCol >= numCols:
            return
        if image[currRow][currCol] != colorToChange:
            return
        if (currRow, currCol) in visited:
            return
        image[currRow][currCol] = newColor
        visited.add((currRow, currCol))
        self.floodHelper(image, currRow - 1, currCol, colorToChange, newColor, visited)
        self.floodHelper(image, currRow + 1, currCol, colorToChange, newColor, visited)
        self.floodHelper(image, currRow, currCol - 1, colorToChange, newColor, visited)
        self.floodHelper(image, currRow, currCol + 1, colorToChange, newColor, visited)

# ===============

from collections import deque

def csFriendCircles(friendships):
    
    '''
    
    [[1,1,0],
     [1,1,0],
     [0,0,1]]
    
    '''
    count = 0
    visited = set()
    l = len(friendships)    
    
    for i in range(l):
        if i not in visited:
            count += 1
            visited.add(i)
            csFriendsCircleHelper(friendships, i, visited)
            
    return count
            
def csFriendsCircleHelper(friendships, currNode, visited):
    for node, edge in enumerate(friendships[currNode]):
        if edge == 1 and node not in visited:
            visited.add(node)
            csFriendsCircleHelper(friendships, node, visited)
