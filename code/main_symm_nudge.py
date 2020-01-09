from colonel_blotto import ColonelBlottoGame
from symmetric_blotto import SymmetricBlotto

from regret_minimization import RegretMinPlayer
from fixed import FixedPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer



game = SymmetricBlotto(5, 3)

trainer = OneShotTrainer(RegretMinPlayer(), RegretMinPlayer(),
                         game,
                         strat_delta=True,
                         plot_regret=True,
                         animate=True, interval=100)

trainer.player_a.regret_sum = [-10, -10, 10, 10, -10]
trainer.player_b.regret_sum = [-10, -10, 10, 10, -10]

trainer.train(5 * 1000)
trainer.save_animation("test.gif", FPS=15)
trainer.report()
