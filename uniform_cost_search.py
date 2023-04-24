#uniform cost search
from puzzle import Puzzle

def uniform_cost_search(start, goal):
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
        
        if (iter % 1000 == 0):
            print("Frontier size={}".format(len(frontier)))
            print("Visited size={}".format(len(visited)))
        
        if current_node.state == goal.state:
            print("Total nodes expanded={}".format(len(visited)))
            print("Final size of frontier={}".format(len(frontier)))
            return current_node
            
        visited.append(current_node)
        
        for i in range(0, 4): #get all child nodes
            new = current_node.move_blank_space(i)
            in_lists = False
            
            if new: #check that this state is not already in lists
                new.parent = current_node
                new.cost = current_node.cost + 1 #add one to cost
                
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

'''
start = Puzzle(['b', '1', '2',
                '4', '5', '3',
                '7', '8', '6'])
'''
start = Puzzle(['8', '7', '1',
                '6', 'b', '2',
                '5', '4', '3'])
#'''
goal = Puzzle(['1', '2', '3',
               '4', '5', '6',
               '7', '8', 'b'])

solution = uniform_cost_search(start, goal)
solution_trace = []
solution_len = 0
 
if solution:
    print('Solution found!')
    
    while solution:
        solution_trace.append(solution)
        solution = solution.parent
        solution_len += 1
        
    while solution_trace:
        solution_trace.pop().print_puzzle()
        print('===')
    
    print('Solution sequence length={}'.format(solution_len))
else:
    print('No solution')