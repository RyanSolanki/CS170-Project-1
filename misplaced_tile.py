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
    
    current_node = start
    frontier.append(current_node) #push start node to frontier
    
    iter = 0
    while True:
        if not frontier:
            return None #problem is impossible to solve
        
        frontier.sort(key = lambda x: x.cost, reverse=True) #order frontier by cost
        current_node = frontier.pop()
        
        #if (iter % 1000 == 0):
        print("Frontier size={}, Visited nodes={}".format(len(frontier), len(visited)), end='\r')
        
        if current_node.state == goal.state:
            print()
            print("Total nodes expanded={}".format(len(visited)))
            print("Final size of frontier={}".format(len(frontier)))
            return current_node
            
        visited.append(current_node)
        
        for i in range(0, 4): #get all child nodes
            new = current_node.move_blank_space(i)
            in_lists = False
            
            if new: #check that this state is not already in lists
                new.parent = current_node

                if(heuistic == "misplaced tile"):
                    new.cost = current_node.cost + 1 + Misplaced_Tile_Heuristic(current_node, goal) #add one to cost
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

def main():

    print("Welcome to 862326974 8 puzzle solver.")
    puzzleSize = int(input("Enter the puzzle size (3 for 8-puzzle, 4 for 15-puzzle, etc.)\n"))
    puzzleType = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
    
    p = Puzzle([0]*(pow(puzzleSize,2)), puzzleSize)
    #p.print_puzzle()
    
    if puzzleType == "1":
        p.update_state(['1', '2', '3', '4', 'b', '5', '6', '7', '8'])
        p.print_puzzle()
    elif puzzleType == "2":
        print("Enter your puzzle, use a zero to represent the blank")
        sNums = []
        for i in range(puzzleSize):
            currentRow = input("Enter the values for row " + str(i + 1) + " separated by spaces\n")
            currentNumString = currentRow.split(" ")
            for string in currentNumString:
                sNums.append(string)
        p.update_state(sNums)
    
    p.print_puzzle()
    
    Astar()

if __name__ == "__main__":
    main()