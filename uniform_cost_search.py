#uniform cost search
from puzzle import Puzzle

def uniform_cost_search(start, goal):
    frontier = []
    visited = []
    max_frontier_size = 0
    
    current_node = start
    frontier.append(current_node) #push start node to frontier

    iter = 0
    while True:
        if not frontier:
            print()
            print(f"To solve this problem the search algorithm expanded a total of {len(visited)} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {max_frontier_size}.")
            print()
            return None #problem is impossible to solve
        
        if(len(frontier) > max_frontier_size):
            max_frontier_size = len(frontier)

        frontier.sort(key = lambda x: x.cost, reverse=True) #order frontier by cost
        current_node = frontier.pop()
        
        if current_node.state == goal.state:
            print()
            print(f"To solve this problem the search algorithm expanded a total of {len(visited)} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {max_frontier_size}.")

            return current_node
            
        visited.append(current_node)
        
        for i in range(0, 4): #get all child nodes
            new = current_node.move_blank_space(i)
            in_lists = False
            
            if new: #check that this state is not already in lists
                new.parent = current_node
                new.g = current_node.g + 1 # update g(n)
                new.cost = new.g # update total cost
                
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