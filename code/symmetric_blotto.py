from colonel_blotto import ColonelBlottoGame

import itertools

class SymmetricBlotto:

    def __init__(self, no_soldiers, no_battlefields):

        self._blotto_instance = ColonelBlottoGame(no_soldiers, no_battlefields)
        self._init_actions()

    def get_utility(self, a_action, b_action):
        aps = list(itertools.permutations(a_action))
        bps = list(itertools.permutations(b_action))

        pairs = list(itertools.product(aps, bps))

        util = 0

        for x, y in pairs:
            util += self._blotto_instance.get_utility(x, y)

        util = util / len(pairs)

        return util

    def get_actions(self):
        return self._actions


    def _init_actions(self):
        # Initializes list of all actions

        actions = self._blotto_instance.get_actions()
        self._actions = sorted(list(set([tuple(sorted(a)) for a in actions])))

if __name__ == "__main__":

    g = ColonelBlottoGame(5, 3)

    actions = g.get_actions()
    actions = set([tuple(sorted(a)) for a in actions])

    actions = sorted(list(actions))

    for i in range(len(actions)):
        for j in range(len(actions)):
            a = actions[i]
            b = actions[j]

            aps = list(itertools.permutations(a))
            bps = list(itertools.permutations(b))

            pairs = list(itertools.product(aps, bps))

            util = 0

            for x, y in pairs:
                util += g.get_utility(x, y)

            util = util / len(pairs)

            print(f"Utility for {a} against {b}: {util}")

        print()


    print(actions)
