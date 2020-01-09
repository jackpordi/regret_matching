import itertools


class ColonelBlottoGame:

    def __init__(self, no_soldiers, no_battlefields):
        assert no_soldiers > no_battlefields
        self.no_soldiers = no_soldiers
        self.no_battlefields = no_battlefields

        self._init_actions()

    # Plays the game and returns the utility for player A
    def get_utility(self, a_action, b_action):

        # Assert same number of battlefields as initialized game
        assert len(a_action) == self.no_battlefields
        assert len(b_action) == self.no_battlefields

        # Asserts each player are using the defined no. of soldiers
        assert sum(a_action) == self.no_soldiers
        assert sum(b_action) == self.no_soldiers

        a_score = 0
        b_score = 0

        for i in range(self.no_battlefields):
            if a_action[i] > b_action[i]:
                a_score = a_score + 1
            elif a_action[i] < b_action[i]:
                b_score = b_score + 1

        if a_score == b_score:
            return 0
        elif a_score > b_score:
            return 1
        else:
            return -1

    def get_actions(self):
        # Returns a list of all possible actions
        # i.e. ways to partition s elements into b sequential boxes
        return self._actions

    def _init_actions(self):
        # Initializes list of all actions

        rng = [i for i in range(self.no_soldiers + 1)] * self.no_battlefields

        permutations = \
            filter(lambda x: sum(x) == self.no_soldiers,
                   list(itertools.permutations(rng, self.no_battlefields)))

        permutations = list(set(permutations))
        permutations.sort()

        self._actions = permutations
        self._actions.sort(key=sorted)
