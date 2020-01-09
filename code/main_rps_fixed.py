from colonel_blotto import ColonelBlottoGame
from symmetric_blotto import SymmetricBlotto

from regret_minimization import RegretMinPlayer
from fixed import FixedPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer


regret_matcher = RegretMinPlayer()
fixed_player = FixedPlayer()

game = RockPaperScissorsGame()

trainer = OneShotTrainer(regret_matcher, fixed_player, game)

fixed_player.strategy = [1, 0 , 0]

trainer.train(1000)
trainer.report()
