#Using node objects to create trees for the puzzles
#Made make_children to create all children from given node, includes move checking and four move operators
#Included functions to calculate the heuristic costs for misplaced tiles and manhattan distance. 
import copy

class Node:
    def __init__(self, puzzle, depth, cost):
        self.puzzle = puzzle
        self.depth = depth
        self.cost = cost
        
    def make_children(self):
        
        children = set()
        temp1 = []
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        idrow = -1
        idcol = -1
        
        #search for the 0 in puzzle
        for i in range(rows):
            for j in range(cols):
                if self.puzzle[i][j] == 0:
                    idrow = i
                    idcol = j
                    
        #up child
        if idrow != 0:
            temp1 = self.puzzle
            temp1[idrow][idcol] = self.puzzle[idrow-1][idcol]
            temp1[idrow-1][idcol] = 0
            children.add(Node(temp1, self.depth+1, self.cost+1))
            
        #down child
        if idrow != 2:
            temp1 = self.puzzle
            temp1[idrow][idcol] = self.puzzle[idrow+1][idcol]
            temp1[idrow+1][idcol] = 0
            children.add(Node(temp1, self.depth+1, self.cost+1))
            
        #left child
        if idcol != 0:
            temp1 = self.puzzle
            temp1[idrow][idcol] = self.puzzle[idrow][idcol-1]
            temp1[idrow][idcol-1] = 0
            children.add(Node(temp1, self.depth+1, self.cost+1))
            
        #right child
        if idcol != 2:
            temp1 = self.puzzle
            temp1[idrow][idcol] = self.puzzle[idrow][idcol+1]
            temp1[idrow][idcol+1] = 0
            children.add(Node(temp1, self.depth+1, self.cost+1)
        
        return children

        
    def misplaced_tiles(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if ((self.puzzle[i][j] != goal[i][j]) and (self.puzzle[i][j] != 0)):
                    count+=1
                    
        return count
                    
    def manhattan(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        total = 0
        
        for i in range(rows):
            for j in range(cols):
                if ((self.puzzle[i][j] != goal[i][j]) and (self.puzzle[i][j] != 0)):
                    temp1 = self.puzzle[i][j]
                    for l in range(rows):
                        for m in range(cols):
                            if temp1 == goal[l][m]:
                                total+=abs(l-i)
                                total+=abs(m-j)
        return total
        
    def solved(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        if(goal == self.puzzle):
            return 1
        else:
            return 0 
                                
        