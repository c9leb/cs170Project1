import queue
from node import Node
import time

# because it sort of acts like a min heap
# Below are some built in puzzles to allow quick testing.
# because it sort of acts like a min heap
# Below are some built in puzzles to allow quick testing.
def main():
    puzzle_row = []
    user_puzzle = []
    puzzle_mode = int(input("What size puzzle would you like to use?" + '\n'))
    print(f"Enter your puzzle, pressing space after each single number and pressing enter when you have entered {puzzle_mode} numbers. Please only enter valid {puzzle_mode*puzzle_mode-1}-puzzles.")
    
    for i in range(puzzle_mode):
        puzzle_row.append(input(f"Enter row {i+1}:"))
        puzzle_row[i] = puzzle_row[i].split()
        
    for i in range(0, puzzle_mode):
        for j in range(0, puzzle_mode):
            puzzle_row[i][j] = int(puzzle_row[i][j])
            
    for i in range(0, puzzle_mode):    
        user_puzzle.append(puzzle_row[i])
        
    select_and_init_algorithm(user_puzzle, puzzle_mode)
        
    

def select_and_init_algorithm(puzzle, dim):
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                      "or (3) the Manhattan Distance Heuristic.\n")
    if algorithm in ("1", "2", "3"):
        uniform_cost_search(puzzle, int(algorithm)-1, dim)

def uniform_cost_search(puzzle, heuristic, dim):
    time1 = time.time()
    goal = Node.goal(dim)
    newNode = Node(puzzle)
    if(heuristic == 0):
        newNode.heur = 0
    if(heuristic == 1):
        newNode.heur = newNode.misplaced_tiles(goal)
    if(heuristic == 2):
        newNode.heur = newNode.manhattan(goal)
        
    working_queue = [newNode]
    repeated_states = []
    repeated_states.append(working_queue[0].puzzle)
    num_nodes_expanded = 0
    max_queue_size = 1
    queue_size = 1
    print()
    
    while True:
        
        check_node = working_queue.pop(0)
    
        print(f"The best node to expand with a g(n) of {check_node.depth} and h(n) of {check_node.heur} is...")
        print_puzzle(check_node.puzzle, dim)
        
        if(check_node.solved(goal)):
            time2 = time.time()
            print()
            print("Goal Found!")
            print(f"Solution depth was: {check_node.depth}")
            print(f"Number of nodes expanded: {num_nodes_expanded}")
            print(f"Max queue size: {max_queue_size}\n")
            print(f"Time: {round(time2 - time1, 3)}\n")
            return
        
        check_node.make_children(repeated_states, heuristic, goal)
        num_nodes_expanded+=1
        
        if(check_node.childup != 0):
            working_queue.append(check_node.childup)
            repeated_states.append(check_node.childup.puzzle)
            
        if(check_node.childdown != 0):
            working_queue.append(check_node.childdown)
            repeated_states.append(check_node.childdown.puzzle)
            
        if(check_node.childleft != 0):
            working_queue.append(check_node.childleft)
            repeated_states.append(check_node.childleft.puzzle)
            
        if(check_node.childright != 0):
            working_queue.append(check_node.childright)
            repeated_states.append(check_node.childright.puzzle)
        
        queue_size = len(working_queue)
        if(queue_size > max_queue_size):
            max_queue_size = queue_size
              
        working_queue.sort(key = lambda x: ((x.depth + x.heur), x.depth))
            

            
def print_puzzle(puzzle, dim):
    for i in range(0, dim):
        print(f"{puzzle[i]}")

if __name__ == "__main__":
    main()