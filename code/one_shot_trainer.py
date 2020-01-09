from matplotlib import pyplot as plt
from celluloid import Camera
from tqdm import trange

import imageio
import numpy as np


class OneShotTrainer:

    def __init__(self,
                 player_a,
                 player_b,
                 game_instance,
                 strat_delta=False,
                 plot_regret=False,
                 interval=1000,
                 animate=False):

        self.player_a = player_a
        self.player_b = player_b

        # Initialize players to know their games
        self.player_a.initialize(game_instance)
        self.player_b.initialize(game_instance)

        self.game_instance = game_instance

        # Animate Strats or not
        self.animate = animate
        if animate:
            self._fig, self._ax = plt.subplots()
            self._camera = Camera(self._fig)
            # Initialize animation graphs
            self._ax.set_xlabel('Strategy')
            self._ax.set_ylabel('Probabilities')
            self._ax.set_title('Strategies by Probability')

        # Plot Regrets or not
        self.plot_regret = plot_regret
        if self.plot_regret:
            self.a_avg_regrets = []
            self.b_avg_regrets = []


        self.games_played = 0
        self.interval = interval


        self.strat_delta = strat_delta
        if strat_delta:

            self.a_last_strat = None
            self.b_last_strat = None

            self.a_delta_history  = []
            self.b_delta_history  = []

    def train(self, iterations):

        for i in trange(iterations):
            self.train_once()

    def train_once(self):
        player_a_strategy = self.player_a.get_action()
        player_b_strategy = self.player_b.get_action()

        result = self.game_instance.get_utility(player_a_strategy,
                                                player_b_strategy)

        self.player_a.post_play(player_b_strategy)
        self.player_b.post_play(player_a_strategy)

        self.games_played += 1



        if self.games_played % self.interval == 0:

            # a_average_strat = self.player_a.get_strategy()
            # b_average_strat = self.player_b.get_strategy()

            a_average_strat = self.player_a.get_average_strategy()
            b_average_strat = self.player_b.get_average_strategy()

            if self.plot_regret:
                a_regret = self.player_a.get_cumulative_regret()
                b_regret = self.player_b.get_cumulative_regret()

                self.a_avg_regrets.append(np.linalg.norm(a_regret))
                self.b_avg_regrets.append(np.linalg.norm(b_regret))

            if self.strat_delta:


                # Plot delta of A strat
                a_strat = np.array(a_average_strat)

                if self.a_last_strat is not None:
                    a_delta = np.linalg.norm(a_strat
                                             - self.a_last_strat)
                    self.a_delta_history.append(a_delta)

                self.a_last_strat = a_strat

                # Plot delta of B strat
                b_strat = np.array(b_average_strat)

                if self.b_last_strat is not None:
                    b_delta = np.linalg.norm(b_strat
                                             - self.b_last_strat)
                    self.b_delta_history.append(b_delta)

                self.b_last_strat = b_strat



            if self.animate:


                index = np.arange(len(a_average_strat))
                width = np.min(np.diff(index))/3

                self._ax.bar(index, a_average_strat, width,
                             color='r',
                             label='Player A')

                self._ax.bar(index + width, b_average_strat, width,
                             color='b',
                             label='Player B')

                self._ax.set_xticks(index + width / 2)
                self._ax.set_xticklabels(self.game_instance.get_actions(), rotation=45)

                self._ax.text(0.05, 0.95, f"Iterations: {self.games_played}", horizontalalignment='left',
                     verticalalignment='center', transform=self._ax.transAxes)



                self._fig.tight_layout()

                self._camera.snap()


    def save_animation(self, filename, FPS=20):
        if not self.animate:
            raise Exception("Animation parameter not set!")

        tmp = 'tmp.gif'

        self._camera.animate().save(tmp, writer = 'imagemagick')

        gif = imageio.mimread(tmp, memtest='2GiB')

        imageio.mimsave(filename, gif, fps=FPS)



    def report(self):

        print("Player A:")
        self.player_a.report()
        a_average_strat = self.player_a.get_average_strategy()
        print("Average Strategy:", a_average_strat)
        print()
        print("Player B:")
        self.player_b.report()
        b_average_strat = self.player_b.get_average_strategy()
        print("Average Strategy:", b_average_strat)

        plt.clf()
        fig, ax = plt.subplots()

        index = np.arange(len(a_average_strat))
        width = np.min(np.diff(index))/3

        ax.bar(index, a_average_strat, width,
               color='r',
               label='Player A')

        ax.bar(index + width, b_average_strat, width,
               color='b',
               label='Player B')

        ax.set_xlabel(f'Strategy')
        ax.set_ylabel('Probabilities')
        ax.set_title(f'Strategies and Probabilities after {self.games_played} iterations')
        ax.set_xticks(index + width / 2)
        ax.set_xticklabels(self.game_instance.get_actions(), rotation=45)
        ax.legend()

        fig.tight_layout()
        plt.show()

        if self.strat_delta:

            plt.clf()

            index = np.arange(1, len(self.a_delta_history) + 1) * self.interval

            fig, ax = plt.subplots()

            ax.plot(index, self.a_delta_history, label="Player A")
            ax.plot(index, self.b_delta_history, label="Player B")
            ax.set_title("Deltas of Average Strategy w.r.t. iterations")

            ax.legend()

            plt.show()

        if self.plot_regret:

            plt.clf()

            index = np.arange(1, len(self.a_avg_regrets) + 1) * self.interval
            fig, ax = plt.subplots()

            ax.plot(index, self.a_avg_regrets, label="Player A")
            ax.plot(index, self.b_avg_regrets, label="Player B")
            ax.legend()

            ax.set_title("Norms of Average Regret w.r.t. iterations")

            plt.show()
