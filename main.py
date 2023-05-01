from puzzle import Puzzle
from uniform_cost_search import *
from misplaced_tile import *
from euclidean_distance import *

def main():
    count = 1
    goal = Puzzle(['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', 'b'])

    print("Welcome to the 8 puzzle solver")
    print("Type '1' to use a default puzzle, type '2' to enter your own")

    p_list = []
    if int(input()) == 2:
        for i in range(0,3):
            temp = input("Row {}: ".format(i))
            if(temp.find(' ') == -1): # Meaning there is no space
                for char in temp:
                    p_list.append(char)
            else:
                arrtemp = temp.split(" ")
                for char in arrtemp:
                    p_list.append(char)
    else:
        p_list = ['b', '1', '2',
                  '4', '5', '3',
                  '7', '8', '6']

    start = Puzzle(p_list)

    print()
    print("Choose the algorithm to use:")
    print("1. Uniform Cost Search")
    print("2. A* (misplaced tile heuristic)")
    print("3. A* (euclidian distance heuristic)")
    algo = int(input())
    print()
    
    solution = None
    solution_trace = []
    solution_len = 0
    
    if (algo == 1):
        solution = uniform_cost_search(start, goal)
    elif (algo == 2):
        solution = Astar(start, goal, "misplaced tile")
    elif (algo == 3):
        solution = Astar(start, goal, "euclidean distance " )
        
    if solution:
        
        while solution:
            solution_trace.append(solution)
            solution = solution.parent
            solution_len += 1
            
        print()
        while solution_trace:
            if(count == 1):
                solution_trace.pop().print_start_state()
            elif(count > 1):
                if(algo == 1):
                    solution_trace.pop().print_ucs()
                else:
                    solution_trace.pop().print_astar()
            count = count + 1
            print()
        
        print("Goal!!!")
        print()
        
        print(f"The depth of the goal node was {solution_len}.")
        print()
    else:
        print("No solution found")
    
if __name__ == "__main__":
    main()