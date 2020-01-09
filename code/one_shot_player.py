class OneShotPlayer(object):

    def __init__(self):
        self.reset_stats()

    def inform(self, utility):
        self.games_played += 1
        self.total_util += utility

    def report(self):
        avg = self.total_util / self.games_played
        return f"Average Utility: {avg} \n" + \
            f"Cumulative Utility: {self.total_util} \n" + \
            f"Games Played: {self.games_played}"

    def games_played(self):
        return self.games_played

    def reset_stats(self):
        self.games_played = 0
        self.total_util = 0
