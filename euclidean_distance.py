from puzzle import Puzzle
import math

    
def Euclidean_Distance_Heuristic(currentPuzzle, goalPuzzle):
    print(currentPuzzle.state)
    print(goalPuzzle.state)
    total_distance = 0
    
    row_length = currentPuzzle.puzzle_size
    print(row_length)
    column_length = currentPuzzle.puzzle_size
    print(column_length)

    current_2d = [[]for x in range(column_length)]
    goal_2d = [[]for x in range(column_length)]

    for i in range(column_length):
        for j in range(row_length):
            tempVal = currentPuzzle.state[i*column_length+j]
            current_2d[i].append(tempVal)
            #print(currentPuzzle.state[i*column_length+j], " CURR")
            #print(current_2d[i][j], "CURRENT")
            tempVal2 = goalPuzzle.state[i*column_length+j]
            #print(goalPuzzle.state[i*column_length+j], " GOAL")
            goal_2d[i].append(tempVal2)
    #print(current_2d)
    #print(goal_2d)
            #print(goal_2d[i][j], "GOAL")

    for i in range(len(current_2d)):
        for j in range(len(current_2d[i])):
            goalIndex = goalPuzzle.state.index(current_2d[i][j])
            goalX = goalIndex/len(current_2d[i])+1
            goalY = goalIndex % len(current_2d[i])+1
            distance = math.sqrt(math.pow(goalX-i, 2)+math.pow(goalY-j, 2))
            total_distance += distance
    return distance

def Astar(start, goal, heuristic):
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

                if(heuristic == "misplaced tile"):
                    new.g = current_node.g + 1 # update g(n)
                    new.h = Misplaced_Tile_Heuristic(current_node, goal) # update h(n)
                    new.cost = new.g + new.h # update new total cost
                else:
                    new.g = current_node.g + 1 # update g(n)
                    new.h = Euclidean_Distance_Heuristic(current_node, goal) # update h(n)
                    new.cost = new.g + new.h # update new total cost
                
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