import numpy as np

from one_shot_player import OneShotPlayer


class RegretMinPlayer(OneShotPlayer):

    def __init__(self):
        super(RegretMinPlayer, self).__init__()
        self.initialized = False

    def initialize(self, game):
        self.game = game
        self.action_list = game.get_actions()
        self.num_actions = len(self.action_list)
        self.regret_sum = [0 for _ in self.action_list]
        self.strategy_sum = [0 for _ in self.action_list]
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

        self._update_regrets(other_player_action)

        self.games_played += 1

        # if self.games_played == 10000:
        #     super(RegretMinPlayer, self).reset_stats()

    def report(self):

        self.check_init()

        print(super(RegretMinPlayer, self).report())

        print(f"Final Regrets: {self.regret_sum}")
        print(f"Final Average Cumulative Regret: {self.get_cumulative_regret()}")

    def _update_regrets(self, other_player_action):

        utilities = [self.game.get_utility(a_action, other_player_action)
                     for a_action in self.action_list]

        played_utility = self.game.get_utility(self.last_action,
                                               other_player_action)

        regrets = [i - played_utility for i in utilities]

        self.regret_sum = [sum(x) for x in zip(self.regret_sum, regrets)]

    def get_action(self):

        self.check_init()

        strategy = self.get_strategy()
        action = self.action_list[np.random.choice(
            len(self.action_list), p=strategy)]
        self.last_action = action

        return action

    def get_strategy(self):


        strategy = [i if i > 0 else 0 for i in self.regret_sum]
        normalizing_sum = sum(strategy)

        if normalizing_sum > 0:
            normalized_strategy = [i / normalizing_sum for i in strategy]
        else:
            normalized_strategy = [1 / self.num_actions for i in strategy]

        self.strategy_sum = [sum(x) for x in
                             zip(self.strategy_sum, normalized_strategy)]

        return normalized_strategy

    def get_average_strategy(self):
        # Returns the average strategy throughout the entire training process

        self.check_init()

        normalizing_sum = sum(self.strategy_sum)

        if normalizing_sum > 0:
            average_strategy = [i / normalizing_sum
                                for i in self.strategy_sum]
        else:
            import pdb; pdb.set_trace()
            average_strategy = [1 / normalizing_sum for
                                _ in range(self.num_actions)]

        return average_strategy

    def get_cumulative_regret(self):
        return sum([i if i > 0 else 0 for i in self.regret_sum]) / super().games_played()
