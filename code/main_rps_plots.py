from colonel_blotto import ColonelBlottoGame
from symmetric_blotto import SymmetricBlotto

from regret_minimization import RegretMinPlayer
from fixed import FixedPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer



game = RockPaperScissorsGame()

trainer = OneShotTrainer(RegretMinPlayer(), RegretMinPlayer(), game,
                         strat_delta=True,
                         plot_regret=True,
                         interval=500,
                         animate=True)

trainer.train(100 * 1000)
trainer.save_animation("rps.gif", FPS=10)
trainer.report()
