class Puzzle:
    def __init__(self, state, **kwargs):
        self.state = state #state array
        self.puzzle_size = 3 #size of one dimension of square puzzle (3 = 3*3 puzzle)
        self.cost = 0
        self.g = 0
        self.h = 0
        
        self.parent = None #append parent for finding solution path
        if 'parent' in kwargs:
            self.parent = kwargs.get('parent')
    
    '''
    moves the blank space 'b' and slides in the correct tile to replace it
    
    argument: direction to move in
    direction notation: 0 = up, 1 = right, 2 = down, 3 = left
    
    returns: a new Puzzle object with the updated state
    '''
    def move_blank_space(self, direction):
        new_state = self.state[:] #copy by value, not reference
    
        blank_location = self.state.index('b') #find index of blank in list
        new_index = 0
        
        if (direction == 0): #up
            if (blank_location < self.puzzle_size): #if impossible to move up
                return None
            else:
                new_index = blank_location - self.puzzle_size
        elif (direction == 1): #right
            if ((blank_location + 1) % self.puzzle_size) == 0:
                return None
            else:
                new_index = blank_location + 1
        elif (direction == 2): #down
            if (blank_location + self.puzzle_size) >= (self.puzzle_size ** 2):
                return None
            else:
                new_index = blank_location + self.puzzle_size
        elif (direction == 3): #left
            if ((blank_location) % self.puzzle_size) == 0:
                return None
            else:
                new_index = blank_location - 1
        else:
            raise ValueError("Move direction cannot be greater than 3 or less than 0")
                
        temp = self.state[new_index]
        new_state[blank_location] = temp
        new_state[new_index] = 'b'
            
        return Puzzle(new_state) #return new puzzle with the move made
    
    '''
    prints the puzzle to console
    '''
    def print_start_state(self):
        print(f"Expanding state")

        for i,tile in enumerate(self.state):
            if i != 0 and (i % self.puzzle_size) == 0:
                print()
            print(tile,end='')
        print()  

    def print_astar(self):

        print(f"The best state to expand with g(n) = {self.g}, h(n) = {self.h} is...")

        for i,tile in enumerate(self.state):
            if i != 0 and (i % self.puzzle_size) == 0:
                print()
            print(tile,end='')
        print("\tExpanding this node...")  

    def print_ucs(self):

        print(f"The best state to expand with g(n) = {self.g} is...")

        for i,tile in enumerate(self.state):
            if i != 0 and (i % self.puzzle_size) == 0:
                print()
            print(tile,end='')
        print("\tExpanding this node...")   
