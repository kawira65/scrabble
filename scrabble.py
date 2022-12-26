import random

class ScrabbleGame:
    def __init__(self, players, board=None):
        self.players = players
        self.board = board if board is not None else self.create_board()
        self.turn = 0
    
    def create_board(self):
        # Create an empty board
        board = [['' for _ in range(15)] for _ in range(15)]
        return board
    
    def get_current_player(self):
        return self.players[self.turn % len(self.players)]
    
    def play_turn(self, word, row, col, direction):
        player = self.get_current_player()
        
        # Place the word on the board
        if direction == 'across':
            for i, letter in enumerate(word):
                self.board[row][col + i] = letter
        elif direction == 'down':
            for i, letter in enumerate(word):
                self.board[row + i][col] = letter
        
        # Update the player's score
        player.score += self.calculate_score(word, row, col, direction)
        
        # Move to the next player's turn
        self.turn += 1
    
    def calculate_score(self, word, row, col, direction):
        score = 0
        for i, letter in enumerate(word):
            # Check for any bonus tiles on the board
            if self.board[row][col] == 'DL':
                score += 2
            elif self.board[row][col] == 'TL':
                score += 3
            elif self.board[row][col] == 'DW':
                score += 2
            elif self.board[row][col] == 'TW':
                score += 3
            else:
                score += 1
            
            # Move to the next tile
            if direction == 'across':
                col += 1
            elif direction == 'down':
                row += 1
        return score

class Player:
    def __init__(self, name, rack):
        self.name = name
        self.rack = rack
        self.score = 0

def create_players(num_players, rack_size=7):
    players = []
    for i in range(num_players):
        rack = draw_tiles(rack_size)
        name = f'Player {i + 1}'
        players.append(Player(name, rack))
    return players

def draw_tiles(num_tiles):
    # Create a list of tiles
    tiles = ['A'] * 9 + ['B'] * 2 + ['C'] * 2 + ['D'] * 4 + ['E'] * 12 + ['F'] * 2 + ['G'] * 3 + ['H'] * 2 + ['I'] * 9 + ['
