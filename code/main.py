from colonel_blotto import ColonelBlottoGame

from regret_minimization import RegretMinPlayer
from fixed import FixedPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer


game = ColonelBlottoGame(5, 3)

p = RegretMinPlayer()

trainer = OneShotTrainer(p, p,
                         game, strat_delta=True, plot_regret=True, interval=1000, animate=False)


trainer.train(1000 * 1000)
# trainer.save_animation("self_play.gif")
trainer.report()
