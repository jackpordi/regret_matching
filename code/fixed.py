import numpy as np

from one_shot_player import OneShotPlayer


class FixedPlayer(OneShotPlayer):

    def __init__(self):
        super(FixedPlayer, self).__init__()
        self.initialized = False

    def initialize(self, game):
        self.game = game
        self.action_list = game.get_actions()
        self.num_actions = len(self.action_list)
        self.strategy = [ 1 / self.num_actions for _ in self.action_list ]
        self.games_played = 0

        self.initialized = True

    def check_init(self):
        if not self.initialized:
            raise Exception('Player not initialized!')

    def post_play(self, other_player_action):

        self.check_init()

        game_result = self.game.get_utility(self.last_action,
                                            other_player_action)
        super().inform(game_result)


        self.games_played += 1


    def report(self):
        print(super(FixedPlayer, self).report())

    def get_action(self):

        strategy = self.strategy
        action = self.action_list[np.random.choice(
            len(self.action_list), p=strategy)]
        self.last_action = action

        return action

    def get_average_strategy(self):
        return self.strategy
