#uniform cost search
from puzzle import Puzzle

def Misplaced_Tile_Heuristic(currentPuzzle, goalPuzzle):
    sum = 0
    for i in range(0, len(currentPuzzle.state)):
        if currentPuzzle.state[i] != goalPuzzle.state[i] and currentPuzzle.state[i] != 'b':
            sum = sum + 1
    return sum
        # for j in range(0, len(currentPuzzle[i])):
        #     if currentPuzzle[i][j] != goalPuzzle[i][j]:
        #         return 1

def Astar(start, goal, heuistic):
    frontier = []
    visited = []
    max_frontier_size = 0
    
    current_node = start
    frontier.append(current_node) #push start node to frontier

    iter = 0
    while True:
        if not frontier:
            return None #problem is impossible to solve
        
        if(len(frontier) > max_frontier_size):
            max_frontier_size = len(frontier)
            
        frontier.sort(key = lambda x: x.cost, reverse=True) #order frontier by cost
        current_node = frontier.pop()
        
        #if (iter % 1000 == 0):
        #print("Frontier size={}, Visited nodes={}".format(len(frontier), len(visited)), end='\r')
        
        if current_node.state == goal.state:
            print()
            print(f"To solve this problem the search algorithm expanded a total of {len(visited)} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {max_frontier_size}.")
            #print("Total nodes expanded={}".format(len(visited)))
            #print("Final size of frontier={}".format(len(frontier)))
            return current_node
            
        visited.append(current_node)
        
        for i in range(0, 4): #get all child nodes
            new = current_node.move_blank_space(i)
            in_lists = False
            
            if new: #check that this state is not already in lists
                new.parent = current_node

                if(heuistic == "misplaced tile"):
                    new.g = current_node.g + 1 # update g(n)
                    new.h = Misplaced_Tile_Heuristic(current_node, goal) # update h(n)
                    new.cost = new.g + new.h # update new total cost
                else:
                    pass #add code for euclidean
                
                in_lists = any(node.state == new.state for node in frontier) #check if already in frontier or visited
                if not in_lists:
                    in_lists = any(node.state == new.state for node in visited)
            
                if not in_lists:
                    frontier.append(new)
                else: #replace if in frontier and higher cost
                    for i,node in enumerate(frontier):
                        if (node.state == new.state) and (new.cost < node.cost):
                            frontier[i] = new
                
        iter += 1