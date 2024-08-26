import random

class Game:
    def __init__(self):
        self.state = {
            'board': [['' for _ in range(5)] for _ in range(5)],
            'players': ['Player1', 'Player2'],
            'turn': 'Player1'
        }
        self.setup_game()

    def setup_game(self):
        # Example setup: place 5 Pawns for each player
        self.state['board'][0] = ['P1'] * 5  # Player1's row
        self.state['board'][4] = ['P2'] * 5  # Player2's row

    def get_state(self):
        return self.state

    def make_move(self, move):
        player, command = move.split(':')
        if player != self.state['turn']:
            return 'Not your turn'

        char, direction = command[0], command[1:]
        if not self.is_valid_move(player, char, direction):
            return 'Invalid move'

        # Example movement logic
        self.apply_move(player, char, direction)
        self.state['turn'] = 'Player2' if self.state['turn'] == 'Player1' else 'Player1'
        return 'Move successful'

    def is_valid_move(self, player, char, direction):
        # Basic validation logic (to be expanded)
        return True

    def apply_move(self, player, char, direction):
        # Basic move application logic (to be expanded)
        pass
