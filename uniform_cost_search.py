#uniform cost search

from puzzle import Puzzle

def uniform_cost_search(start, goal):
    print("TODO: implement me!")
    
    frontier = []
    visited = []
    
    current_node = start
    frontier.insert(0,current_node) #push start node to frontier
    
    iter = 0
    while True:
        if not frontier:
            return None #problem is impossible to solve
        
        current_node = frontier.pop()
        
        print("Current iteration={}".format(iter))
        current_node.print_puzzle()
        
        if current_node.state == goal.state:
            return current_node #todo: return a sequence or something
            
        visited.append(current_node)
        
        for i in range(0, 4): #get all child nodes
            new = current_node.move_blank_space(i)
            in_lists = False
            if new: #check that this state is not already in lists
                new.parent = current_node
                
                for node in frontier:
                    if node.state == new.state:
                        in_lists = True
                        break
                
                for node in visited:
                    if node.state == new.state:
                        in_lists = True
                        break
            
                if not in_lists:
                    frontier.insert(0, new)
                else:
                    current_node = new
        
        iter += 1
        
start = Puzzle(['8', '7', '1',
                '6', 'b', '2',
                '5', '4', '3'])
                
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