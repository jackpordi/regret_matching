from colonel_blotto import ColonelBlottoGame
from symmetric_blotto import SymmetricBlotto

from regret_minimization import RegretMinPlayer
from fixed import FixedPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer



game = RockPaperScissorsGame()

trainer = OneShotTrainer(RegretMinPlayer(), RegretMinPlayer(), game)

trainer.train(100 * 1000)
trainer.report()
