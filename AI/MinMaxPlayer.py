from player import Player

class MinMaxPlayer(Player):

    def __init__(self, color, no, game_state):
        super().__init__(color, no)
        self.state = game_state

