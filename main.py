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
    
#         colorToChange = image[sr][sc]
#         queue = deque()
#         queue.append((sr, sc))
#         visited = set()
#         numRows, numCols = len(image), len(image[0])
        
#         while len(queue) > 0:
#             currPixel = queue.popleft()
#             if currPixel in visited:
#                 continue
#             currRow, currCol = currPixel[0], currPixel[1]
#             image[currRow][currCol] = newColor
#             visited.add(currPixel)
            
#             topRow = currRow - 1
#             if topRow >= 0 and image[topRow][currCol] == colorToChange:
#                 queue.append((topRow, currCol))
                
#             bottomRow = currRow + 1
#             if bottomRow < numRows and image[bottomRow][currCol] == colorToChange:
#                 queue.append((bottomRow, currCol))
                
#             leftCol = currCol - 1
#             if leftCol >= 0 and image[currRow][leftCol] == colorToChange:
#                 queue.append((currRow, leftCol))
                
#             rightCol = currCol + 1
#             if rightCol < numCols and image[currRow][rightCol] == colorToChange:
#                 queue.append((currRow, rightCol))
                
#         return image


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
