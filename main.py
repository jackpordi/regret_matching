from colonel_blotto import ColonelBlottoGame

from regret_minimization import RegretMinPlayer

from rock_paper_scissors import RockPaperScissorsGame

from one_shot_trainer import OneShotTrainer


game = ColonelBlottoGame(5, 3)
# game = RockPaperScissorsGame()

trainer = OneShotTrainer(RegretMinPlayer, RegretMinPlayer,
                         game)

trainer.train(100000)
trainer.report()
