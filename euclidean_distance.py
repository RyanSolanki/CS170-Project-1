from puzzle import Puzzle
from uniform_cost_search import *
from misplaced_tile import *
import math

def singleIndexTo2D(index, row_length, column_length):
    return (index // column_length, index % row_length)

    
def Euclidean_Distance_Heuristic(currentPuzzle, goalPuzzle):
    #print(currentPuzzle.state)
    #print(goalPuzzle.state)
    total_distance = 0
    
    row_length = currentPuzzle.puzzle_size
    #print(row_length)
    column_length = currentPuzzle.puzzle_size
    #print(column_length)

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
    # for arr in current_2d:
    #     print(arr)
    #     print()
    # print()
    # for arr in goal_2d:
    #     print(arr)
    #     print()

    for i in range(len(current_2d)):
        for j in range(len(current_2d[i])):
            if(current_2d[i][j] != 'b'):
                # print(f"CURRENT value at {i},{j} is {current_2d[i][j]}")
                goalIndex = goalPuzzle.state.index(current_2d[i][j])
                indicies = singleIndexTo2D(goalIndex, row_length, column_length)
                goalI = indicies[0]#goalIndex/len(current_2d[i])+1
                goalJ = indicies[1]#goalIndex % len(current_2d[i])+1
                # print(f"GOAL value at {goalI},{goalJ} is {goal_2d[goalI][goalJ]}")
                distance = math.sqrt(math.pow(goalI-i, 2)+math.pow(goalJ-j, 2))
                # print(f"Distance: {distance}")
                total_distance += distance
                # print(f"Total Distance: {total_distance}")
                # print()
    return total_distance

# samplePuzzle = [[1,2,3],[4,5,6],[7,8,'b']]
# index2d = singleIndexTo2D([1,2,3,4,5,6,7,8,'b'].index(6), 3, 3)
# print(f"2d Index: {index2d}, resulting part of the puzzle: {samplePuzzle[index2d[0]][index2d[1]]}")
# print(Euclidean_Distance_Heuristic(Puzzle(['b',8,7,6,5,4,3,2,1]), Puzzle([1,2,3,4,5,6,7,8,'b'])))

def Astar(start, goal, heuristic):
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