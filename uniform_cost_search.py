#uniform cost search
from puzzle import Puzzle

def uniform_cost_search():
    print("TODO: implement me!")

def Misplaced_Tile_Heuristic():
    print("TODO: implement me!")

def Astar():
    print("TODO: implement me!")

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