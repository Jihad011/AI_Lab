class State:
    def __init__(self, initial_board=None):
        self.board = initial_board if initial_board else [7,2,4,5,0,6,8,3,1]  # Initial board state
        self.space_pos = self.board.index(0)  # Position of empty space (0)
        self.goal = [0,1,2,3,4,5,6,7,8]  # Goal state matches the image
        
    def copy(self):
        new_state = State()
        new_state.board = self.board.copy()
        new_state.space_pos = self.space_pos
        return new_state
    
    def get_possible_moves(self):
        moves = []
        row = self.space_pos // 3
        col = self.space_pos % 3
        
        # Check all possible moves (up, down, left, right)
        if row > 0: moves.append('up')
        if row < 2: moves.append('down')
        if col > 0: moves.append('left')
        if col < 2: moves.append('right')
        
        return moves
    
    def move(self, direction):
        new_state = self.copy()
        row = self.space_pos // 3
        col = self.space_pos % 3
        
        if direction == 'up' and row > 0:
            new_pos = self.space_pos - 3
        elif direction == 'down' and row < 2:
            new_pos = self.space_pos + 3
        elif direction == 'left' and col > 0:
            new_pos = self.space_pos - 1
        elif direction == 'right' and col < 2:
            new_pos = self.space_pos + 1
        else:
            return None
            
        # Swap the empty space with the number
        new_state.board[new_state.space_pos] = new_state.board[new_pos]
        new_state.board[new_pos] = 0
        new_state.space_pos = new_pos
        
        return new_state
    
    def is_goal(self):
        return self.board == self.goal
    
    def __str__(self):
        output = ""
        for i in range(9):
            if i > 0 and i % 3 == 0:
                output += "\n"
            if self.board[i] == 0:
                output += "  _"
            else:
                output += f"  {self.board[i]}"
        return output

    def get_solution_path(self):
        """Find solution path using BFS"""
        from collections import deque
        visited = set()
        queue = deque([(self, [])])
        
        while queue:
            current_state, path = queue.popleft()
            board_tuple = tuple(current_state.board)
            
            if current_state.is_goal():
                return path
                
            if board_tuple not in visited:
                visited.add(board_tuple)
                
                for move in current_state.get_possible_moves():
                    next_state = current_state.move(move)
                    if next_state:
                        queue.append((next_state, path + [move]))
        
        return None  # No solution found
        
    def apply_solution(self, solution_path):
        """Apply a sequence of moves to reach the solution"""
        if not solution_path:
            return None
            
        current = self
        for move in solution_path:
            current = current.move(move)
        return current


