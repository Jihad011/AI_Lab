from state import State
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_instructions():
    print("\n8-Puzzle Game")
    print("=============")
    print("Use the following commands to play:")
    print("  U: Move up")
    print("  D: Move down")
    print("  L: Move left")
    print("  R: Move right")
    print("  h: Show solution")
    print("  q: Quit")
    print("\nTry to arrange the numbers in order:")
    print("1 2 3\n4 5 6\n7 8 _\n")

def main():
    current_state = State()
    player_moves = 0
    solution_moves = 0
    
    while True:
        clear_screen()
        print_instructions()
        print("\nCurrent board:")
        print(current_state)
        print(f"\nPlayer moves: {player_moves}")
        if solution_moves > 0:
            print(f"Solution moves: {solution_moves}")
        
        if current_state.is_goal():
            print("\nCongratulations! You solved the puzzle!")
            break
            
        command = input("\nEnter move (U/D/L/R), h for solution, or q to quit: ").lower()
        
        if command == 'q':
            print("Thanks for playing!")
            break
        elif command == 'h':
            solution = current_state.get_solution_path()
            if solution:
                print("\nSolution found! Here are the moves:")
                print(" -> ".join(solution))
                print("\nWould you like to see the solution played out? (y/n)")
                if input().lower() == 'y':
                    for move in solution:
                        clear_screen()
                        print(f"Applying move: {move}")
                        current_state = current_state.move(move)
                        solution_moves += 1
                        print(current_state)
                        print(f"\nPlayer moves: {player_moves}")
                        print(f"Solution moves: {solution_moves}")
                        import time
                        time.sleep(1)  # Pause to show each move
                    print("\nFinal state (Goal state):")
                    print(current_state)
                    print(f"\nPuzzle solved with {solution_moves} solution moves!")
                print("\nPress Enter to continue playing...")
            else:
                print("\nNo solution found for current state!")
                print("Press Enter to continue...")
            input()
            continue
            
        direction = {
            'u': 'up',
            'd': 'down',
            'l': 'left',
            'r': 'right'
        }.get(command)
        
        if direction in current_state.get_possible_moves():
            current_state = current_state.move(direction)
            player_moves += 1
        else:
            input("Invalid move! Press Enter to continue...")

if __name__ == "__main__":
    main()

