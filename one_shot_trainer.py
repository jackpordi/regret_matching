from matplotlib import pyplot as plt

import numpy as np


class OneShotTrainer:

    def __init__(self, player_a_class, player_b_class, game_instance):
        self.player_a = player_a_class(game_instance)
        self.player_b = player_b_class(game_instance)
        self.game_instance = game_instance

    def train(self, iterations):

        for i in range(iterations):
            player_a_strategy = self.player_a.get_action()
            player_b_strategy = self.player_b.get_action()
            print("Player A plays", player_a_strategy)
            print("Player B plays", player_b_strategy)

            result = self.game_instance.get_utility(player_a_strategy,
                                                    player_b_strategy)

            if result == 1:
                print("Player A has won!")
            elif result == -1:
                print("Player B has won!")
            else:
                print("Draw")

            self.player_a.post_play(player_b_strategy)
            self.player_b.post_play(player_a_strategy)

            print()

    def report(self):

        print("Player A's wins, loses and draws:")
        self.player_a.report()
        a_average_strat = self.player_a.get_average_strategy()
        print("Average Strategy:", a_average_strat)
        print()
        print("Player B's wins, loses and draws:")
        self.player_b.report()
        b_average_strat = self.player_b.get_average_strategy()
        print("Average Strategy:", b_average_strat)

        a_strat_sorted = sorted(a_average_strat, reverse=True)
        b_strat_sorted = [x for _, x in sorted(zip(a_average_strat,
                                                   b_average_strat),
                                               reverse=True)]
        actions_sorted = \
            [x for _, x
             in sorted(zip(a_average_strat,
                           self.game_instance.get_actions()), reverse=True)]

        fig, ax = plt.subplots()

        index = np.arange(len(a_average_strat))
        width = np.min(np.diff(index))/3

        ax.bar(index, a_strat_sorted, width,
               color='r',
               label='Player A')

        ax.bar(index + width, b_strat_sorted, width,
               color='b',
               label='Player B')

        ax.set_xlabel('Strategy')
        ax.set_ylabel('Probabilities')
        ax.set_title('Strategies by Probability')
        ax.set_xticks(index + width / 2)
        ax.set_xticklabels(actions_sorted, rotation=45)
        ax.legend()

        fig.tight_layout()
        plt.show()
