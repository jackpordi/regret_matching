class OneShotPlayer(object):

    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0

    def won(self):
        self.wins = self.wins + 1

    def lost(self):
        self.losses = self.losses + 1

    def draw(self):
        self.draws = self.draws + 1

    def report(self):
        return self.wins, self.losses, self.draws
