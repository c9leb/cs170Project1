#Using node objects to create trees for the puzzles
#Made make_children to create all children from given node, includes move checking and four move operators
#Included functions to calculate the heuristic costs for misplaced tiles and manhattan distance. 
import copy

class Node:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.depth = 0
        self.heur = 0
        self.childup = 0
        self.childdown = 0
        self.childleft = 0
        self.childright = 0
    
    #misplaced tiles funtion to calculate the heuristic cost of a given node         
    def misplaced_tiles(self, goal):
        rows = len(self.puzzle)
        cols = len(self.puzzle[0])
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if ((self.puzzle[i][j] != goal[i][j]) and (self.puzzle[i][j] != 0)):
                    count+=1
                    
        return count
    
    #manhattan distance funtion to calculate the heuristic cost of a given node                
    def manhattan(self, goal):
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
    
    #makes children for each operator and sets them to the children of self
    #takes in parent node, set of already expanded nodes, wanted heuristic to calculate heuristic cost and goal state          
    def make_children(self, expanded, heuristic, goal):
        
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
            temp1 = copy.deepcopy(self.puzzle)
            temp1[idrow][idcol] = self.puzzle[idrow-1][idcol]
            temp1[idrow-1][idcol] = 0
            if(Node.convert(temp1) not in expanded):
                self.childup = (Node(temp1))
                self.childup.depth = self.depth + 1
                if(heuristic == 0):
                    self.childup.heur = 0
                if(heuristic == 1):
                    self.childup.heur = self.childup.misplaced_tiles(goal)
                if(heuristic == 2):
                    self.childup.heur = self.childup.manhattan(goal)
            
        #down child
        if idrow != 2:
            temp2 = copy.deepcopy(self.puzzle)
            temp2[idrow][idcol] = self.puzzle[idrow+1][idcol]
            temp2[idrow+1][idcol] = 0
            if(Node.convert(temp2) not in expanded):
                self.childdown = (Node(temp2))
                self.childdown.depth = self.depth + 1
                if(heuristic == 0):
                    self.childdown.heur = 0
                if(heuristic == 1):
                    self.childdown.heur = self.childdown.misplaced_tiles(goal)
                if(heuristic == 2):
                    self.childdown.heur = self.childdown.manhattan(goal)
            
        #left child
        if idcol != 0:
            temp3 = copy.deepcopy(self.puzzle)
            temp3[idrow][idcol] = self.puzzle[idrow][idcol-1]
            temp3[idrow][idcol-1] = 0
            if(Node.convert(temp3) not in expanded):
                self.childleft = (Node(temp3))
                self.childleft.depth = self.depth + 1
                if(heuristic == 0):
                    self.childleft.heur = 0
                if(heuristic == 1):
                    self.childleft.heur = self.childleft.misplaced_tiles(goal)
                if(heuristic == 2):
                    self.childleft.heur = self.childleft.manhattan(goal)
            
        #right child
        if idcol != 2:
            temp4 = copy.deepcopy(self.puzzle)
            temp4[idrow][idcol] = self.puzzle[idrow][idcol+1]
            temp4[idrow][idcol+1] = 0
            if(Node.convert(temp4) not in expanded):
                self.childright = (Node(temp4))
                self.childright.depth = self.depth + 1
                if(heuristic == 0):
                    self.childright.heur = 0
                if(heuristic == 1):
                    self.childright.heur = self.childright.misplaced_tiles(goal)
                if(heuristic == 2):
                    self.childright.heur = self.childright.manhattan(goal)
                
        
        return

    #checks self puzzle against goal puzzle
    def solved(self, goal):
        if(goal == self.puzzle):
            return 1
        else:
            return 0 
                  
    def goal(dim):
        #used matrix creation from - https://www.geeksforgeeks.org/python-matrix-creation-of-nn/
        #set last element to 0 to match goal state
        g = [list(range(1 + dim * i, 1 + dim * (i + 1))) for i in range(dim)]
        g[dim-1][dim-1] = 0
        return g              
    
    #converts a the puzzle to a tuple to be used in a set - used material from https://www.geeksforgeeks.org/python-convert-list-of-lists-to-tuple-of-tuples/
    def convert(puzzle):
        return(tuple(tuple(i) for i in puzzle))                  
        