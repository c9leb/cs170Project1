import queue
from node import Node
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#       sleeping cat
#         |\      _,,,---,,_
#   ZZZzz /,`.-'`'    -.  ;-;;,_
#        |,4-  ) )-,_. ,\ (  `'-'
#       '---''(_/--'  `-'\_)  

# test puzzles from sample code provided by professor Keogh
#used Jupyer Lab 
puzzles = [[[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]],
           [[1, 2, 3], 
            [4, 5, 6], 
            [0, 7, 8]],
           [[1, 2, 3], 
            [5, 0, 6], 
            [4, 7, 8]],
           [[1, 3, 6], 
            [5, 0, 2], 
            [4, 7, 8]],
           [[1, 3, 6], 
            [5, 0, 7], 
            [4, 8, 2]],
           [[1, 6, 7], 
            [5, 0, 3], 
            [4, 8, 2]],
           [[7, 1, 2], 
            [4, 8, 5], 
            [6, 3, 0]],
           [[0, 7, 2], 
            [4, 6, 1], 
            [3, 5, 8]]]
             
data1 = [[], [], [], []]
data2 = [[], [], [], []]
data3 = [[], [], [], []]

def main():
    puzzle_row = []
    user_puzzle = []
    #takes input
    #puzzle_mode = int(input("What size puzzle would you like to use?" + '\n'))
    puzzle_mode = 3
    for i in range(8):
        select_and_init_algorithm(puzzles[i], puzzle_mode)
        print(f"print with puzzle {i+1}")
        #select_and_init_algorithm(puzzles[i], puzzle_mode)
    #print(f"Enter your puzzle, pressing space after each single number and pressing enter when you have entered {puzzle_mode} numbers. Please only enter valid {puzzle_mode*puzzle_mode-1}-puzzles.")
    
    #modifies input to make it work with functions
    #for i in range(puzzle_mode):
    #    puzzle_row.append(input(f"Enter row {i+1}:"))
    #    puzzle_row[i] = puzzle_row[i].split()
        
    #changes split chars into ints    
    #for i in range(0, puzzle_mode):
    #    for j in range(0, puzzle_mode):
    #        puzzle_row[i][j] = int(puzzle_row[i][j])
            
    #appends each row to user_puzzle        
    #for i in range(0, puzzle_mode):    
    #    user_puzzle.append(puzzle_row[i])
        
    #select_and_init_algorithm(user_puzzle, puzzle_mode)
        
    
#used for selecting which algorithm the user wants
def select_and_init_algorithm(puzzle, dim):
    #algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
    #                  "or (3) the Manhattan Distance Heuristic.\n")
    for i in range(3):
        uniform_cost_search(puzzle, i, dim)

#our search function to find the goal state, takes in the input puzzle, input algorithm, and puzzle dimensions as arguments
def uniform_cost_search(puzzle, heuristic, dim):
    #start timer
    time1 = time.time()
    
    #creates goal state
    goal = Node.goal(dim)
    
    #creates parent node
    newNode = Node(puzzle)
    
    #sets heuristic cost of parent node for output purposes
    if(heuristic == 0):
        newNode.heur = 0
    if(heuristic == 1):
        newNode.heur = newNode.misplaced_tiles(goal)
    if(heuristic == 2):
        newNode.heur = newNode.manhattan(goal)
        
    working_queue = [newNode]
    repeated_states = set()
    repeated_states.add(Node.convert(working_queue[0].puzzle))
    num_nodes_expanded = 0
    max_queue_size = 1
    queue_size = 1
    print()
    
    #while loop will always run until goal state is found
    while True:
        
        #pops off the first node of the queue
        check_node = working_queue.pop(0)
    
        #print(f"The best node to expand with a g(n) of {check_node.depth} and h(n) of {check_node.heur} is...")
        #print_puzzle(check_node.puzzle, dim)
        
        #checks solved node and outputs statistics regarding the tree and time elapsed
        if(check_node.solved(goal)):
            time2 = time.time()
            #print()
            #print("Goal Found!")
            #print(f"Solution depth was: {check_node.depth}")
            if(heuristic == 0):
                data1[0].append(check_node.depth)
                data1[1].append(num_nodes_expanded)
                data1[2].append(max_queue_size)
                data1[3].append(round(time2 - time1, 9))
            if(heuristic == 1):
                data2[0].append(check_node.depth)
                data2[1].append(num_nodes_expanded)
                data2[2].append(max_queue_size)
                data2[3].append(round(time2 - time1, 9))
            if(heuristic == 2):
                data3[0].append(check_node.depth)
                data3[1].append(num_nodes_expanded)
                data3[2].append(max_queue_size)
                data3[3].append(round(time2 - time1, 9))
            return
        
        #makes children with four movement operators up, down, left, right, and calculates the heuristics for each
        check_node.make_children(repeated_states, heuristic, goal)
        num_nodes_expanded+=1
        
        #adds each child to the working queue and adds it to the repeated states queue
        #repeated states stops already expanded nodes from being expanded
        if(check_node.childup != 0):
            working_queue.append(check_node.childup)
            repeated_states.add(Node.convert(check_node.childup.puzzle))
            
        if(check_node.childdown != 0):
            working_queue.append(check_node.childdown)
            repeated_states.add(Node.convert(check_node.childdown.puzzle))
            
        if(check_node.childleft != 0):
            working_queue.append(check_node.childleft)
            repeated_states.add(Node.convert(check_node.childleft.puzzle))
            
        if(check_node.childright != 0):
            working_queue.append(check_node.childright)
            repeated_states.add(Node.convert(check_node.childright.puzzle))
            
        #checks max queue size and readjusts accordingly
        queue_size = len(working_queue)
        if(queue_size > max_queue_size):
            max_queue_size = queue_size
            
        #sorts working queue by the heuristic function + depth and if they are equal, will sort equal values by depth      
        working_queue.sort(key = lambda x: ((x.depth + x.heur), x.depth))
            

#puzzle print fn           
def print_puzzle(puzzle, dim):
    for i in range(0, dim):
        print(f"{puzzle[i]}")

if __name__ == "__main__":
    main()