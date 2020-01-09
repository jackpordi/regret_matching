class RockPaperScissorsGame:

    _actions = ("ROCK", "PAPER", "SCISSORS")
    _name = "Rock, Paper Scissors"

    # Plays the game and returns the utility for player A
    def get_utility(self, a_action, b_action):

        assert a_action in RockPaperScissorsGame._actions
        assert b_action in RockPaperScissorsGame._actions

        a_index = RockPaperScissorsGame._actions.index(a_action)
        b_index = RockPaperScissorsGame._actions.index(b_action)
        diff = a_index - b_index

        utility = diff if abs(diff) == 1 else int(diff // -2)

        return utility

    def get_actions(self):
        return list(RockPaperScissorsGame._actions)
